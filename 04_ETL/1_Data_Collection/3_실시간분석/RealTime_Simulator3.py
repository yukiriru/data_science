# 업비트 실시간 가격 모니터링 시스템
import threading
import time
import pandas as pd
import requests
import matplotlib
import random

# GUI 백엔드 설정 (환경별 최적화)
try:
    matplotlib.use("TkAgg")
except:
    try:
        matplotlib.use("Qt5Agg")
    except:
        matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import warnings

# 한글 폰트 설정 (OS별 설정)
font_location = "C:\Windows\Fonts\malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
rc('font',family=font_name)
plt.rcParams['axes.unicode_minus'] = False

# ===== 공유 데이터와 동기화 =====
df = pd.DataFrame(columns=["t", "value", "timestamp", "change_rate"])
lock = threading.Lock()
stop_event = threading.Event()

# ===== 업비트 REST API 설정 =====
session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
})

UPBIT_TICKER_URL = "https://api.upbit.com/v1/ticker"
AVAILABLE_MARKETS = ["KRW-XRP", "KRW-BTC", "KRW-ETH", "KRW-ADA", "KRW-DOT"]
CURRENT_MARKET = "KRW-BTC"


def price_collector(market=CURRENT_MARKET) -> tuple:
    """업비트에서 현재가와 변화율 가져오기"""
    try:
        r = session.get(UPBIT_TICKER_URL, params={"markets": market}, timeout=5)
        r.raise_for_status()
        data = r.json()
        if not data:
            raise RuntimeError("empty ticker response")
        ticker = data[0]
        price = float(ticker["trade_price"])

        # 변화율과 변화 방향 확인
        change_rate = float(ticker.get("change_rate", 0)) * 100
        change = ticker.get("change", "EVEN")  # RISE: 상승, FALL: 하락, EVEN: 보합

        # 하락 시 음수로 변환
        if change == "FALL":
            change_rate = -abs(change_rate)
        elif change == "RISE":
            change_rate = abs(change_rate)
        else:
            change_rate = 0

        timestamp = time.strftime("%H:%M:%S")
        return price, change_rate, timestamp
    except Exception as e:
        print(f"API 호출 오류: {e}")
        return None, None, None


def get_available_markets():
    """사용 가능한 마켓 목록 조회"""
    try:
        r = session.get("https://api.upbit.com/v1/market/all", timeout=5)
        r.raise_for_status()
        markets = r.json()
        krw_markets = [m["market"] for m in markets if m["market"].startswith("KRW-")]
        return krw_markets[:10]
    except:
        return AVAILABLE_MARKETS


# ===== 수집기(백그라운드 쓰레드) =====
def collector():
    """2초마다 업비트 현재가 수집"""
    t = 0
    consecutive_errors = 0

    while not stop_event.is_set():
        try:
            price, change_rate, timestamp = price_collector(CURRENT_MARKET)
            if price is not None:
                with lock:
                    df.loc[len(df)] = {
                        "t": t,
                        "value": price,
                        "timestamp": timestamp,
                        "change_rate": change_rate
                    }
                # 콘솔 출력 시 변화율 올바르게 표시
                if change_rate > 0:
                    print(f"[{timestamp}] {CURRENT_MARKET}: {price:,.0f}원 (+{change_rate:.2f}%)")
                elif change_rate < 0:
                    print(f"[{timestamp}] {CURRENT_MARKET}: {price:,.0f}원 ({change_rate:.2f}%)")
                else:
                    print(f"[{timestamp}] {CURRENT_MARKET}: {price:,.0f}원 (0.00%)")
                consecutive_errors = 0
            else:
                consecutive_errors += 1
                if consecutive_errors >= 3:
                    print("연속적인 API 오류로 임시 데이터 사용")
                    # 임시 데이터 생성
                    with lock:
                        if len(df) > 0:
                            last_price = df.iloc[-1]["value"]
                            # 마지막 가격 기준 ±2% 범위에서 랜덤
                            noise_price = last_price * (1 + random.uniform(-0.02, 0.02))
                            noise_change = random.uniform(-5, 5)
                        else:
                            noise_price = 1000 + random.randint(-100, 100)
                            noise_change = 0
                        df.loc[len(df)] = {
                            "t": t,
                            "value": noise_price,
                            "timestamp": time.strftime("%H:%M:%S"),
                            "change_rate": noise_change
                        }
        except Exception as e:
            print(f"수집 오류: {e}")
            consecutive_errors += 1

        t += 1
        time.sleep(2)


# ===== 시뮬레이션 실행 =====
def run_simulation():
    """실시간 가격 차트 시뮬레이션"""
    global df

    # 데이터 초기화
    with lock:
        df = df.iloc[0:0].copy()

    # 수집 쓰레드 시작
    stop_event.clear()
    th = threading.Thread(target=collector, daemon=True)
    th.start()

    print(f"\n{CURRENT_MARKET} 실시간 모니터링을 시작합니다...")
    print("그래프 창을 닫으면 모니터링이 종료됩니다.")

    try:
        # 그래프 초기화
        plt.ion()
        fig, ax = plt.subplots(figsize=(12, 8))

        ax.set_ylabel("가격 (원)", fontsize=12)
        ax.set_xlabel("시간(초)", fontsize=12)
        ax.grid(True, alpha=0.3)

        WINDOW = 60  # 최근 60개 포인트 표시

        while not stop_event.is_set():
            try:
                with lock:
                    local = df.tail(WINDOW).copy()

                if len(local) > 0:
                    x = local["t"].values
                    y = local["value"].values
                    change_rates = local["change_rate"].values

                    # 현재 변화율에 따라 색상 결정
                    current_change_rate = change_rates[-1] if len(change_rates) > 0 else 0
                    line_color = 'red' if current_change_rate >= 0 else 'blue'

                    # 그래프 다시 그리기 (색상 변경)
                    ax.clear()
                    ax.set_ylabel("가격 (원)", fontsize=12)
                    ax.set_xlabel("시간(초)", fontsize=12)
                    ax.grid(True, alpha=0.3)

                    # 변화율에 따른 색상으로 그래프 그리기
                    ax.plot(x, y, color=line_color, linewidth=2, label='현재가')
                    ax.legend()

                    if len(x) > 0:
                        ax.set_xlim(max(0, x[0] - 1), x[-1] + 1)

                    # Y축 자동 스케일 (가격 범위에 맞춰)
                    if len(y) > 0:
                        ymin, ymax = min(y), max(y)
                        margin = (ymax - ymin) * 0.05 if ymax > ymin else ymax * 0.01
                        ax.set_ylim(ymin - margin, ymax + margin)

                    # 최신 정보 표시
                    latest = local.iloc[-1]
                    change_rate = latest['change_rate']

                    if change_rate > 0:
                        change_text = f"+{change_rate:.2f}%"
                        title_color = 'black'
                    elif change_rate < 0:
                        change_text = f"{change_rate:.2f}%"
                        title_color = 'black'
                    else:
                        change_text = "0.00%"
                        title_color = 'black'

                    ax.set_title(
                        f"{CURRENT_MARKET} | 현재가: {latest['value']:,.0f}원 | 전일대비: {change_text} | {latest['timestamp']}",
                        fontsize=14, fontweight='bold', color=title_color)

                plt.tight_layout()
                fig.canvas.draw()
                fig.canvas.flush_events()
                time.sleep(0.5)  # 화면 갱신 주기

            except Exception as e:
                print(f"차트 업데이트 오류: {e}")
                break

    except Exception as e:
        print(f"시뮬레이션 오류: {e}")
    finally:
        print("\n모니터링을 종료합니다...")
        stop_event.set()
        th.join(timeout=3)
        plt.ioff()
        try:
            plt.close('all')
        except Exception:
            pass


# ===== 마켓 변경 기능 =====
def change_market():
    """모니터링할 마켓 변경"""
    global CURRENT_MARKET
    print("\n사용 가능한 마켓 목록:")
    markets = get_available_markets()
    for i, market in enumerate(markets[:10], 1):
        current = " (현재 선택됨)" if market == CURRENT_MARKET else ""
        print(f"{i:2d}. {market}{current}")

    try:
        choice = int(input("\n변경할 마켓 번호를 입력하세요: ")) - 1
        if 0 <= choice < len(markets):
            CURRENT_MARKET = markets[choice]
            print(f"마켓이 {CURRENT_MARKET}로 변경되었습니다.")
        else:
            print("올바른 번호를 입력하세요.")
    except ValueError:
        print("숫자를 입력하세요.")


# ===== 현재 시세 조회 =====
def show_current_price():
    """현재 시세 정보 표시"""
    print(f"\n{CURRENT_MARKET} 현재 시세 조회 중...")
    price, change_rate, timestamp = price_collector(CURRENT_MARKET)

    if price is not None:
        # 변화율 올바르게 표시
        if change_rate > 0:
            change_text = f"+{change_rate:.2f}%"
        elif change_rate < 0:
            change_text = f"{change_rate:.2f}%"
        else:
            change_text = "0.00%"

        print(f"현재가: {price:,.0f}원")
        print(f"전일 대비: {change_text}")
        print(f"조회 시간: {timestamp}")
    else:
        print("시세 정보를 가져올 수 없습니다.")


# ===== 메뉴 출력 =====
def print_main_menu():
    print("\n" + "=" * 50)
    print("업비트 실시간 가격 모니터링 시스템")
    print("=" * 50)
    print(f"현재 모니터링: {CURRENT_MARKET}")
    print("-" * 50)
    print("1. 실시간 모니터링 시작")
    print("2. 현재 시세 조회")
    print("3. 모니터링 마켓 변경")
    print("4. 종료")
    print("* 엔터: 메뉴 새로고침")
    print("=" * 50)


# ===== 메인 루프 =====
if __name__ == "__main__":
    print(f"시스템 초기화... (Backend: {matplotlib.get_backend()})")

    while True:
        print_main_menu()
        print("메뉴 선택: ", end="")
        selection = input()

        if selection == "":
            continue

        try:
            menu_num = int(selection)
        except ValueError:
            print("숫자를 입력하세요.")
            continue

        if menu_num == 1:
            run_simulation()
        elif menu_num == 2:
            show_current_price()
        elif menu_num == 3:
            change_market()
        elif menu_num == 4:
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 메뉴를 선택하세요.")