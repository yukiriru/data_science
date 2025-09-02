# 목적: 파이썬 코드를 활용하여 OpenAPI 호출 자동화
# Step1: OpenAPI를 제공하는 사이트에서 제공하는 샘플 프로그램을 확보한다.

#파라메터 세팅
# params ={키1:값1, .... , 키N:값N  }
#
# response = requests.get(url, params=params)
# print(response.content)
import requests
import json
import pandas as pd

access_key = '8917a575c7fd4b2196863298e2f49e3fe86c2f1e28a8e33dfb5bf6077884f3ba'
def get_request_url():
    url = 'http://apis.data.go.kr/1160100/service/GetStockSecuritiesInfoService/getStockPriceInfo'
    params = {'serviceKey': access_key ,
              'resultType' : 'json',
              'numOfRows' : 5,
              'pageNo':10
              }
    response = requests.get(url, params=params)
    return response.text

raw_str_json = get_request_url()

print(raw_str_json)
print(type(raw_str_json)) # 응답받은 데이터는 문자열이기 때문에 JSON 타입으로 변경을 해야한다.

raw_json = json.loads(raw_str_json)
print(type(raw_json))

print(raw_json['response']['body']['items']['item'])
raw_json = json.loads(raw_str_json)
items = raw_json['response']['body']['items']['item']

df = pd.DataFrame(items,columns=['basDt','srtnCd','itmsNm'])
print(df.head())