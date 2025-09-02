import requests
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from datetime import datetime, timedelta

# 폰트 설정
font_location = r"C:\Windows\Fonts\malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
rc('font', family=font_name)
plt.rcParams['axes.unicode_minus'] = False

access_key = "8917a575c7fd4b2196863298e2f49e3fe86c2f1e28a8e33dfb5bf6077884f3ba"

url = "http://apis.data.go.kr/1160100/service/GetStockSecuritiesInfoService/getStockPriceInfo"

# **종목 코드를 매핑하는 딕셔너리**
# **실제 사용 시, 이 부분을 정확하게 확인해야 합니다.**
stock_codes = {
    "삼성전자": "KR7005930003",
    "NAVER": "KR7035420009",
    "카카오": "KR7035720002",
    "SK하이닉스": "KR7000660001",
}


def fetch_stock_one_day(date_yyyymmdd: str, item_code: str, timeout=(10, 30)):
    """
    단일 날짜, 단일 종목의 주식 정보를 API로부터 가져오는 함수 (종목 코드로 조회).
    """
    params = {
        "serviceKey": access_key,
        "resultType": "json",
        "basDt": date_yyyymmdd,
        "isinCd": item_code,  # **수정된 부분: 종목명 대신 종목 코드 사용**
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
    if isinstance(item, list):
        item = item[0]
    return item
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from datetime import datetime, timedelta

# 폰트 설정
font_location = r"C:\Windows\Fonts\malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
rc('font', family=font_name)
plt.rcParams['axes.unicode_minus'] = False

access_key = "8917a575c7fd4b2196863298e2f49e3fe86c2f1e28a8e33dfb5bf6077884f3ba"

url = "http://apis.data.go.kr/1160100/service/GetStockSecuritiesInfoService/getStockPriceInfo"

# **종목 코드를 매핑하는 딕셔너리**
# **실제 사용 시, 이 부분을 정확하게 확인해야 합니다.**
stock_codes = {
    "삼성전자": "KR7005930003",
    "NAVER": "KR7035420009",
    "카카오": "KR7035720002",
    "SK하이닉스": "KR7000660001",
}

def fetch_stock_one_day(date_yyyymmdd: str, item_code: str, timeout=(10, 30)):
    """
    단일 날짜, 단일 종목의 주식 정보를 API로부터 가져오는 함수 (종목 코드로 조회).
    """
    params = {
        "serviceKey": access_key,
        "resultType": "json",
        "basDt": date_yyyymmdd,
        "isinCd": item_code, # **수정된 부분: 종목명 대신 종목 코드 사용**
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
    if isinstance(item, list):
        item = item[0]
    return item

def get_stock_df(start_date: str, end_date: str, item_names: list[str]) -> pd.DataFrame:
    """
    지정된 기간 동안의 여러 종목 주식 데이터를 DataFrame으로 반환하는 함수.
    """
    start = datetime.strptime(start_date, "%Y-%m-%d").date()
    end   = datetime.strptime(end_date,   "%Y-%m-%d").date()
    rows = []

    d = start
    while d <= end:
        basDt = d.strftime("%Y%m%d")
        for name in item_names:
            code = stock_codes.get(name) # **수정된 부분: 종목명으로 코드 가져오기**
            if not code:
                print(f"[WARN] {name}에 대한 종목 코드를 찾을 수 없습니다. 스킵합니다.")
                continue

            try:
                item = fetch_stock_one_day(basDt, code) # **수정된 부분: 종목 코드 사용**
                if not item:
                    continue
                rows.append({
                    "날짜": pd.to_datetime(item.get("basDt"), format="%Y%m%d"),
                    "종목명": item.get("itmsNm"), # API 응답에서 종목명 사용
                    "시장": item.get("mrktCtg"),
                    "종가": pd.to_numeric(item.get("clpr"), errors="coerce"),
                    "시가총액": pd.to_numeric(item.get("mrktTotAmt"), errors="coerce"),
                })
            except requests.exceptions.RequestException as e:
                print(f"[WARN] {basDt} {name} ({code}) 요청 실패: {e}")
        d += timedelta(days=1)

    if not rows:
        return pd.DataFrame(columns=["날짜","종목명","시장","종가","시가총액"])

    df = pd.DataFrame(rows)
    df = df.sort_values(["종목명", "날짜"]).reset_index(drop=True)
    df = df.set_index("날짜")
    return df

# === 예시 ===
item_names = ["카카오", "NAVER", "삼성전자"]
start_date = "2024-08-20"
end_date = "2024-08-31"

df = get_stock_df(start_date, end_date, item_names)
print(df.to_string())

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


def get_stock_df(start_date: str, end_date: str, item_names: list[str]) -> pd.DataFrame:
    """
    지정된 기간 동안의 여러 종목 주식 데이터를 DataFrame으로 반환하는 함수.
    """
    start = datetime.strptime(start_date, "%Y-%m-%d").date()
    end = datetime.strptime(end_date, "%Y-%m-%d").date()
    rows = []

    d = start
    while d <= end:
        basDt = d.strftime("%Y%m%d")
        for name in item_names:
            code = stock_codes.get(name)  # **수정된 부분: 종목명으로 코드 가져오기**
            if not code:
                print(f"[WARN] {name}에 대한 종목 코드를 찾을 수 없습니다. 스킵합니다.")
                continue

            try:
                item = fetch_stock_one_day(basDt, code )  # **수정된 부분: 종목 코드 사용**
                if not item:
                    continue
                rows.append({
                    "날짜": pd.to_datetime(item.get("basDt"), format="%Y%m%d"),
                    "종목명": item.get("itmsNm"),  # API 응답에서 종목명 사용
                    "시장": item.get("mrktCtg"),
                    "종가": pd.to_numeric(item.get("clpr"), errors="coerce"),
                    "시가총액": pd.to_numeric(item.get("mrktTotAmt"), errors="coerce"),
                })
            except requests.exceptions.RequestException as e:
                print(f"[WARN] {basDt} {name} ({code}) 요청 실패: {e}")
        d += timedelta(days=1)

    if not rows:
        return pd.DataFrame(columns=["날짜", "종목명", "시장", "종가", "시가총액"])

    df = pd.DataFrame(rows)
    df = df.sort_values(["종목명", "날짜"]).reset_index(drop=True)
    df = df.set_index("날짜")
    return df


# === 예시 ===
item_names = ["삼성전자", "NAVER", "카카오", "SK하이닉스"]
start_date = "2024-08-25"
end_date = "2024-08-31"

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