import requests
import json
from datetime import datetime, timedelta

access_key = '8917a575c7fd4b2196863298e2f49e3fe86c2f1e28a8e33dfb5bf6077884f3ba'

def get_request(base_date, day_time):
    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst'
    params = {
        'serviceKey': access_key,
        'dataType': 'JSON',
        'base_date': base_date,
        'base_time': day_time,
        'nx': 55,
        'ny': 127
    }
    r = requests.get(url, params=params)
    return json.loads(r.text)

# 현재 시각
now = datetime.now()
base_date = now.strftime("%Y%m%d")
day_time = now.strftime("%H%M")

# 첫 호출
raw_json = get_request(base_date, day_time)

# body가 없으면 1시간 전으로 보정
if "body" not in raw_json.get("response", {}):
    print('갱신 시간이 아니므로 시간 보정을 합니다.')
    now = now - timedelta(hours=1)
    base_date = now.strftime("%Y%m%d")
    day_time = now.strftime("%H%M")
    raw_json = get_request(base_date, day_time)

# 결과 출력
print("base_date:", base_date, "day_time:", day_time)
print(raw_json)
