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

def get_request_url(year_start, year_end, month_end):
    url = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'

    data = []

    for year in range(year_start, year_end + 1): # range 객체의 두번째 인자 값은 포함하지 않기 때문에 1을 더해줌
        # 이 프로그램은 year_stat 1월 ~ 12월 까지
        # year_end 1월 부터 month_end월까지 자동으로 요청을 만드는 반복문 조건입니다.
        # 만약에 함수 파라메터가 2022, 2023, 5 이렇게 호출될경우
        # 2022년 1월 2022년 12월, 2023년 1월 부터 2023년 5월까지 호출하는 조건이 된다.
        # 그렇게 때문에 마지막 년도를 제외한 월의 조건 12가 되기 위한 3항 연산 조건
        month_end_value = 12 if year < year_end else month_end
        for month in range(1, month_end_value + 1):
            # 6자리 연월을 계산하기 위해
            ym = year * 100 + month # 2023*100=202300, month:5 =>202300+5=202305

            params = {
                'serviceKey': access_key,
                '_type': 'json',
                'YM': ym,
                'NAT_CD': 100,
                'ED_CD': 'D'
            }

            response = requests.get(url, params=params)
            raw_json = response.json()

            if 'items' in raw_json['response']['body']:
                items = raw_json['response']['body']['items']['item']
                data.append([
                        pd.to_datetime(items['ym'], format='%Y%m'),
                        items['natKorNm'],
                        items['num']
                    ])

    df = pd.DataFrame(data, columns=['날짜', '국가', '여행자수'])
    df = df.set_index('날짜')
    return df
# 특정시작년도 부터 특정년도의 특정월까지의 데이터를 수집
df = get_request_url(2023,2024,6)

print(df)
