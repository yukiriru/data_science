# 05_realtime_simulation_menu.py
# 메뉴 구조와 쓰레드 사용 방식은 원본 OpenAPI 스케줄러와 동일 컨셉.
# 1번: 실시간 시뮬레이션 (수집 쓰레드: 2초마다 데이터 추가, 메인 스레드: 라인 차트 갱신)
import threading
import time

import matplotlib
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# GUI 백엔드 고정 (Windows/Anaconda 환경에서 가장 호환성 좋음)
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_location = r"C:\Windows\Fonts\malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
rc('font', family=font_name)
plt.rcParams['axes.unicode_minus'] = False

# ===== 공유 데이터와 동기화 객체 =====
df = pd.DataFrame(columns=["time", "num"])
lock = threading.Lock()
stop_event = threading.Event()


# ===== 수집기(백그라운드 쓰레드): 2초마다 데이터 1행 추가 =====
def collector():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    url = 'https://www.worldometers.info/kr/'
    driver.get(url)
    while not stop_event.is_set():
        with lock:
            driver.implicitly_wait(5)
            items = driver.find_elements(By.CSS_SELECTOR, '#tablemore tbody tr:nth-child(14) td div span')
            raw = items[0].text.replace(',', '')
            if raw.isdigit():
                now = int(time.time() % 3600)
                df.loc[len(df)] = {'time': now, 'num': int(raw)}
                print(now, raw)
        time.sleep(2)


# ===== 시뮬레이션 실행(메인 스레드에서 그림 갱신) =====
def run_simulation():
    # 기존 데이터 초기화
    global df
    with lock:
        df = df.iloc[0:0].copy()

    # 수집 쓰레드 시작
    stop_event.clear()
    th = threading.Thread(target=collector, daemon=True)
    th.start()

    # 그래프 초기화 (라인 객체 1번만 만들고 데이터만 업데이트: 고성능)
    plt.ion()
    fig, ax = plt.subplots(figsize=(7, 4))
    (line,) = ax.plot([], [], marker="o")
    ax.set_title("실시간 수집 시뮬레이션 (2초마다 갱신)")
    ax.set_xlabel("time")
    ax.set_ylabel("num")
    ax.set_ylim(3_271_470_458, 3_271_543_210)

    WINDOW = 50  # 최근 N개만 보여주는 슬라이딩 윈도우

    try:
        # 창이 열려 있는 동안 주기적으로 화면 갱신
        while plt.fignum_exists(fig.number):
            with lock:
                local = df.tail(WINDOW).copy()

            x = local["time"].to_list()
            y = local["num"].to_list()

            line.set_data(x, y)
            if x:
                ax.set_xlim(max(0, x[0] - 1), x[-1] + 1)
                ax.set_ylim(max(3271470458, y[0] - 1), y[-1] + 1)

            fig.canvas.draw()
            fig.canvas.flush_events()
            time.sleep(0.2)  # 화면 갱신 주기(수집은 2초마다)
    finally:
        # 창을 닫으면 안전 종료
        stop_event.set()
        th.join(timeout=3)
        plt.ioff()
        try:
            plt.close(fig)
        except Exception:
            pass


# ===== 메뉴 출력 =====
def print_main_menu():
    print("\n< 실시간 수집 시뮬레이터 ver1.0 >")
    print("\n1. 실시간 수집 시뮬레이션 실행 (2초마다 갱신)")
    print("2. 업데이트 예정")
    print("3. 종료")
    print("* 엔터: 메뉴 업데이트\n")


# ===== 메인 루프 (원본과 동일한 입력 방식) =====
if __name__ == "__main__":
    while True:
        print_main_menu()
        print("아래행에 메뉴입력: ", end="")
        selection = input()
        if selection == "":
            continue
        else:
            try:
                menu_num = int(selection)
            except ValueError:
                print("숫자를 입력하세요.")
                continue

        if menu_num == 1:
            # 그림 갱신은 메인 스레드에서 수행해야 하므로
            # 여기서 run_simulation()을 직접 호출(블로킹) 후 종료 시 메뉴로 복귀
            run_simulation()
        elif menu_num == 2:
            print("업데이트 예정중입니다.")
        elif menu_num == 3:
            print("프로그램을 종료합니다.")
            break
        elif menu_num == 0:
            continue
