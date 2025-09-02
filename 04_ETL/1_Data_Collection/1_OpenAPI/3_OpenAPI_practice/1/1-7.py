import requests
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from datetime import datetime, timedelta
from urllib.parse import quote_plus

font_location = r"C:\Windows\Fonts\malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
rc('font', family=font_name)
plt.rcParams['axes.unicode_minus'] = False

access_key = "8917a575c7fd4b2196863298e2f49e3fe86c2f1e28a8e33dfb5bf6077884f3ba"  # 예: '...'

url = "http://apis.data.go.kr/1160100/service/GetStockSecuritiesInfoService/getStockPriceInfo"

def fetch_stock_one_day(date_yyyymmdd: str, item_name: str, timeout=(10, 30)):
    encoded_item_name = quote_plus(item_name)

    params = {
        "serviceKey": access_key,
        "resultType": "json",
        "basDt": date_yyyymmdd, #기준일자
        "itmsNm":encoded_item_name, #종목명
        "numOfRows": 1,
        "pageNo": 1,
    }
    response = requests.get(url, params=params, timeout=timeout)
    response.raise_for_status()
    j = response.json()
    body = j.get("response", {}).get("body", {})
    items = body.get("items", {})
    item = items.get("item")
    if not item:
        return None
    # item 이 리스트/단일 객체일 수 있어 방어
    if isinstance(item, list):
        item = item[0]
    return item

def get_stock_df(start_date: str, end_date: str, item_names: list[str]) -> pd.DataFrame:
    """
    start_date, end_date: 'YYYY-MM-DD' 형식
    item_names: 종목명 리스트 (예: ['삼성전자', 'NAVER', '카카오'])
    반환: 날짜-종목별 종가/거래량 등으로 구성된 DataFrame
    """
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
                    "날짜": pd.to_datetime(item.get("basDt"), format="%Y%m%d"),
                    "종목명": item.get("itmsNm"),
                    "시장": item.get("mrktCtg"),
                    "종가": pd.to_numeric(item.get("clpr"), errors="coerce"),
                    # "시가": pd.to_numeric(item.get("mkp"), errors="coerce"),
                    # "고가": pd.to_numeric(item.get("hipr"), errors="coerce"),
                    # "저가": pd.to_numeric(item.get("lopr"), errors="coerce"),
                    # "대비": pd.to_numeric(item.get("vs"), errors="coerce"),
                    # "등락률(%)": pd.to_numeric(item.get("fltRt"), errors="coerce"),
                    # "거래량": pd.to_numeric(item.get("trqu"), errors="coerce"),
                    # "거래대금": pd.to_numeric(item.get("trPrc"), errors="coerce"),
                    "시가총액": pd.to_numeric(item.get("mrktTotAmt"), errors="coerce"),
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

# === 예시 ===
item_names = ["삼성전자", "NAVER", "카카오","SK하이닉스"]     # 원하면 다른 종목명으로 변경
start_date = "2025-08-25"
end_date   = "2025-08-31"

df = get_stock_df(start_date, end_date, item_names)
print(df.head())

# ===== 시각화 - 종목별 종가 추이 차트 =====
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
