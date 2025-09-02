# 목적: 파이썬 코드를 활용하여 OpenAPI 호출 자동화
# Step1: OpenAPI를 제공하는 사이트에서 제공하는 샘플 프로그램을 확보한다.

#파라메터 세팅
# params ={키1:값1, .... , 키N:값N  }
#
# response = requests.get(url, params=params)
# print(response.content)
import requests
# 인코딩키가 되지 않으면 디코딩키로 할 것
access_key = '8917a575c7fd4b2196863298e2f49e3fe86c2f1e28a8e33dfb5bf6077884f3ba'
def get_request_url():
    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst'
    params = {'serviceKey': access_key ,
              'dataType' : 'JSON',
              'base_date' : '20250828',
              'base_time':'1217',
              'nx':55,
              'ny':127
              }
    response = requests.get(url, params=params)
    return response.text

raw_str_json = get_request_url()
print(raw_str_json)