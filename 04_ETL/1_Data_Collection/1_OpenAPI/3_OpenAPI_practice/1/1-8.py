import requests
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from datetime import datetime, timedelta
import xml.etree.ElementTree as ET

font_location = r"C:\Windows\Fonts\malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
rc('font', family=font_name)
plt.rcParams['axes.unicode_minus'] = False

access_key = "8917a575c7fd4b2196863298e2f49e3fe86c2f1e28a8e33dfb5bf6077884f3ba"  # 예: '...'

url = "http://apis.data.go.kr/1160100/service/GetStockSecuritiesInfoService/getStockPriceInfo"

def fetch_stock_one_day(date_yyyymmdd: str, item_name: str, timeout=(10, 30)):
    """
    특정 일자(basDt) + 종목명(itmsNm)으로 1건 조회를 시도.
    반환: dict 또는 None
    """
    params = {
        "serviceKey": access_key,
        "resultType": "xml",
        "basDt": date_yyyymmdd, #기준일자
        "itmsNm": item_name, #종목명
        "numOfRows": 1,
        "pageNo": 1,
    }
    response = requests.get(url, params=params, timeout=timeout)
    response.raise_for_status()
    root = ET.fromstring(response.text)
    items = root.find(".//items")
    if items is None:
        return None
    item = items.find("item")
    return item

def get_stock_df(start_date: str, end_date: str, item_names: list[str]) -> pd.DataFrame:

    start = datetime.strptime(start_date, "%Y-%m-%d").date()
    end   = datetime.strptime(end_date,   "%Y-%m-%d").date()
    rows = []

    # 날짜 (1일  단위)
    d = start
    while d <= end:
        basDt = d.strftime("%Y%m%d")
        for name in item_names:
            try:
                item = fetch_stock_one_day(basDt, name)
                if not item:
                    continue # 해당일에 데이터가 없으면 스킵
                # 주요 필드 (공식 가이드 참고)  # :contentReference[oaicite:2]{index=2}
                rows.append({
                    "날짜": pd.to_datetime(item.findtext("basDt"), format="%Y%m%d", errors="coerce"),
                    "종목명": (item.findtext("itmsNm") or "").strip(),
                    "시장": (item.findtext("mrktCtg") or "").strip(),
                    "종가": pd.to_numeric(item.findtext("clpr"), errors="coerce"),
                    "시가총액": pd.to_numeric(item.findtext("mrktTotAmt"), errors="coerce"),
                })
            # 예외 ( 타임아웃  /  네트워크 등 )
            except requests.exceptions.RequestException as e:
                print(f"[WARN] {basDt} {name} 요청 실패: {e}")
        d += timedelta(days=1)

    if not rows:
        return pd.DataFrame(columns=["날짜","종목명","시장","종가","시가총액"])

    df = pd.DataFrame(rows)
    df = df.sort_values(["종목명", "날짜"]).reset_index(drop=True)
    df = df.set_index("날짜")
    return df

# 예시
item_names = ["삼성전자", "NAVER", "카카오"]
start_date = "2025-08-25"
end_date   = "2025-08-31"

df = get_stock_df(start_date, end_date, item_names)
print(df.to_string())

# ===== 시각화 (종목별 종가 라인 차트) =====
plt.figure(figsize=(11, 6))
for name in df["종목명"].unique():
    subset = df[df["종목명"] == name]
    plt.plot(subset.index, subset["종가"], label=name)

plt.xlabel("날짜")
plt.ylabel("종가")
plt.title(f"{start_date} ~ {end_date} 종목별 종가 추이")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
