# 목적: 시간정보 파라메터를 현재 시간 정보를 통해 자동 생성

import requests
import json
import time

access_key = '8917a575c7fd4b2196863298e2f49e3fe86c2f1e28a8e33dfb5bf6077884f3ba'

def get_request_url():
    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst'
    params = {'serviceKey': access_key ,
              'dataType' : 'JSON',
              'base_date' : base_date ,
              'base_time': day_time,
              'nx':55,
              'ny':127
              }
    response = requests.get(url, params=params)
    return response.text

# 호출 직전에 현재 시간 정보 구하기
base_date = time.strftime("%Y%m%d")
day_time = time.strftime("%H%M")


raw_str_json = get_request_url()

print(raw_str_json)
print(type(raw_str_json)) # 응답받은 데이터는 문자열이기 때문에 JSON 타입으로 변경을 해야한다.

# 실데이터 추출을 위해 dict(json)타입으로 변경
raw_json = json.loads(raw_str_json)
print(type(raw_json))

# 실데이터 추출
print(raw_json['response']['body']['items']['item'])
