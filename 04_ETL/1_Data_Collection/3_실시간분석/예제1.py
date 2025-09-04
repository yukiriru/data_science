from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import re
import time

URL = "https://www.worldometers.info/kr/"

def get_driver(headless=False):
    options = Options()
    # options.add_argument("--headless=new")  # 필요 시 주석 해제 (화면 없이 실행)
    options.add_argument("--disable-gpu")
    options.add_argument("--start-maximized")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome Safari"
    )
    return webdriver.Chrome(options=options)  # Selenium Manager (경로 지정 X)

def get_military_spending(driver, timeout=10, retries=3):
    for attempt in range(retries):
        try:
            counter = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, 'span.rts-counter[rel="gov_expenditures_military"]')
                )
            )
            raw_text = counter.get_attribute("textContent").strip()
            number_str = re.sub(r"[^\d]", "", raw_text)
            value = int(number_str) if number_str else None
            return value, raw_text
        except Exception:
            if attempt < retries - 1:
                time.sleep(0.5)  # 재시도 전 잠깐 대기
                continue
            else:
                raise

def main(interval_sec=5, iterations=10):
    driver = get_driver(headless=False)
    try:
        driver.get(URL)
        # 페이지 전체 카운터가 보일 때까지 초기 대기
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span.rts-counter"))
        )

        for i in range(iterations):
            ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            value = get_military_spending(driver)
            raw = value.replace(",","")
            print(f"[{ts}] 오늘 지출된 군사비: {value:,} (raw: {raw})")
            time.sleep(interval_sec)

    finally:
        driver.quit()

if __name__ == "__main__":
    # 5초마다 10번 출력 (총 50초 실행)
    main(interval_sec=5)
