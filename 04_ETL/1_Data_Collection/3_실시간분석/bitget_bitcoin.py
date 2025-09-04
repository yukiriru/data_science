import requests
import time
from datetime import datetime

BASE_URL = "https://api.bitget.com"
SYMBOL = "BTCUSDT"

def get_spot_ticker(symbol):
    url = f"{BASE_URL}/api/v2/spot/market/tickers"
    params = {"symbol": symbol}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json().get("data", [])
        if data:
            ticker = data[0]
            return ticker.get("lastPr")  # 현재가
    return None

# === 3초마다 반복 조회 (시간 포함) ===
while True:
    price = get_spot_ticker(SYMBOL)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 현재 시각 (YYYY-MM-DD HH:MM:SS)
    if price:
        print(f"[{now}] ✅ {SYMBOL} 현재가: {price} USDT")
    else:
        print(f"[{now}] ❌ 가격 조회 실패")
    time.sleep(3)
