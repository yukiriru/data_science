#기본 요청 검증
#2012년 1월의 내국인 출입국 관광객수
# http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList?YM=201201&NAT_CD=100&ED_CD=D&serviceKey=

# 최신데이터 검증
# 2025년 6월의 내국인 출입국 관광객수
# http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList?YM=202506&NAT_CD=100&ED_CD=D&serviceKey=
# JSON 응답 검증
# 공공데이터 포탈인 경우 _type=json 추가
# http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList?YM=202506&NAT_CD=100&ED_CD=D&_type=json&serviceKey=

# 쿼리파라메터 정리
# 고정값은 앞에 변동 값은 뒤에
# http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList?&_type=json&serviceKey=&YM=202506&NAT_CD=100&ED_CD=D

# 기타 쿼리 검증
# 2024년 6월 미국인 관광객수
# http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList?_type=json&serviceKey=&YM=202406&NAT_CD=275&ED_CD=E