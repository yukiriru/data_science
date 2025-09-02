# 목적: 시간정보 파라메터를 현재 시간 정보를 통해 자동 생성

import requests
import json
import time
import pandas as pd
from datetime import datetime, timedelta

access_key = '8917a575c7fd4b2196863298e2f49e3fe86c2f1e28a8e33dfb5bf6077884f3ba'
# http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst
def get_request_url():
    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
    params = {'serviceKey': access_key ,
              'dataType' : 'JSON',
              'base_date' : base_date ,
              'base_time': day_time,
              'nx':55,
              'ny':127
              }
    response = requests.get(url, params=params)
    return json.loads(response.text)

# 호출 직전에 현재 시간 정보 구하기
now = datetime.now()
base_date = time.strftime("%Y%m%d")
day_time = time.strftime("%H%M")

raw_json = get_request_url()

if "body" not in raw_json.get("response", {}):
    print('갱신 시간이 아니므로 시간 보정을 합니다.')
    now = now - timedelta(hours=1)
    base_date = now.strftime("%Y%m%d")
    day_time = now.strftime("%H%M")
    raw_json = get_request_url(base_date, day_time)

# 실데이터 추출
parsed_json = raw_json['response']['body']['items']['item']
df = pd.DataFrame(parsed_json)
print(df)
