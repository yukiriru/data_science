a= 1

def vartest(a):
    a = a + 1   # 매개변수 a는 로컬 변수, 로컬 스코프 유지
    return a  # 이 시점에 로컬 변수 a 는 2

a=vartest(a) # 로컬변수 a의 2의 결과를 글로벌 변수 a로 치환
print(a) # 이 시점에서 a는 치환된 글로벌 a를 본다. 로컬변수 a(X)