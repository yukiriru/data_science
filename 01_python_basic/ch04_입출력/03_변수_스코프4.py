a= 1

def vartest(a):
    a = a + 1   # 매개변수 a는 로컬 변수, 로컬 스코프 유지
    return a  # 이 시점에 로컬 변수 a 는 2

vartest(a) # 로컬변수 a의 2의 결과를 글로벌 변수 a로 받지 않음
print(a) # 이 시점에서 a는 글로벌 a를 본다.