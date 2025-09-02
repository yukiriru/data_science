import requests
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from xml.etree.ElementTree import fromstring

# 한글 폰트 설정
font_location = "C:\Windows\Fonts\malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
rc('font', family=font_name)
plt.rcParams['axes.unicode_minus'] = False

access_key = '8917a575c7fd4b2196863298e2f49e3fe86c2f1e28a8e33dfb5bf6077884f3ba'

def get_request_url(year_start, year_end, month_end, foreign_countrys):
    count = 1
    url = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'

    data = []
    for country in foreign_countrys:
        for year in range(year_start, year_end + 1):
            month_end_value = 12 if year < year_end else month_end
            for month in range(1, month_end_value + 1):
                ym = year * 100 + month

                params = {
                    'serviceKey': access_key,
                    'YM': ym,
                    'NAT_CD': country,
                    'ED_CD': 'E' # 외래 관광객
                }

                response = requests.get(url, params=params)
                xml_root = fromstring(response.text)

                if xml_root:

                    data.append([
                            pd.to_datetime(xml_root.find('body').find('items').find('item').find('ym').text, format='%Y%m'),
                            xml_root.find('body').find('items').find('item').find('natKorNm').text,
                            xml_root.find('body').find('items').find('item').find('num').text
                        ])
                    print(f'{count}건 데이터 수집중...')
                    count=count+1

    df = pd.DataFrame(data, columns=['날짜', '국가', '방문자수'])
    df = df.set_index('날짜')
    return df
#112:중국
#130:일본
#275:미국
foreign_countrys = [112,130,275]
year_start = 2023
year_end = 2023
month_end = 3
# df = get_request_url(2018, 2024, 1, foreign_countrys)
df = get_request_url(year_start, year_end, month_end, foreign_countrys)

# 그래프 크기 설정
plt.figure(figsize=(10, 6))

# 국가별 선 그래프 그리기
for country in df['국가'].unique():
    country_data = df[df['국가'] == country]
    plt.plot(country_data.index, country_data['방문자수'], label=country)

# 그래프 축 레이블 및 타이틀 설정
plt.xlabel('날짜')
plt.ylabel('여행자수')
plt.title(f'{year_start}년 1월부터 {year_end}년 {month_end}월까지 대한민국 관광객 방문자수')

# 범례 추가
plt.legend()

# x축 눈금 라벨 회전
plt.xticks(rotation=45)

# 그래프 출력
plt.show()
