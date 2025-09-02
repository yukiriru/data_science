a= 1

def vartest(a):
    a = a + 1   # 매개변수 a는 로컬 변수, 로컬 스코프 유지
    # return a

# a = vartest(a)
vartest(a)
print(a) # 이 시점에서 a는 글로벌 a를 본다.