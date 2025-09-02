def vartest():
    # 로직 수행
    result = 100

vartest()
# 글로벌 스코프에서 로컬 스코프 변수 참조 위배
# 로컬 변수는 함수 수행이후 사라지는 변수이기 때문에 참조 불가능하다.
print(result)