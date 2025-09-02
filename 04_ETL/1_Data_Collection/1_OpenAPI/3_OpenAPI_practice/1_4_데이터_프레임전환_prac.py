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
    url = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'
    params = {'serviceKey': access_key ,
              '_type' : 'json',
              'YM' : 202305,
              'NAT_CD':100,
              'ED_CD':'D'
              }
    response = requests.get(url, params=params)
    return response.text

# raw_str_json = get_request_url()
raw_str_json = """{"response":{"header":{"resultCode":"0000","resultMsg":"OK"},"body":{"items":{"item":{"ed":"국민해외관광객","edCd":"D","natCd":100,"natKorNm":"한  국","num":1683022,"rnum":1,"ym":202305}},"numOfRows":10,"pageNo":1,"totalCount":1}}}
"""
print(raw_str_json)
print(type(raw_str_json)) # 응답받은 데이터는 문자열이기 때문에 JSON 타입으로 변경을 해야한다.

raw_json = json.loads(raw_str_json)
print(type(raw_json))

print(raw_json['response']['body']['items']['item'])

data = []
# [
#   [ ] : 행데이터
#]
#
parsed_json = raw_json['response']['body']['items']['item']
# 분석할 데이터 컬럼 선택
data.append([
    pd.to_datetime(parsed_json['ym'], format="%Y%m"), # 시계열 데이터 문자열을 날짜 타입으로 변경
    parsed_json['natKorNm'], parsed_json['num']
])

df = pd.DataFrame(data=data, columns=['날짜','국가','여행자수'])
df = df.set_index("날짜") # 시계열 분석을 위해서 날짜 열을 행의 인덱스로 전환
print(df)
