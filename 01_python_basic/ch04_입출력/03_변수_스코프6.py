a= 1

def vartest():
    # 로컬스코프에서 글로벌 스코프 변수
    # 읽기는 가능하다.
    b = a   # 글로벌 스코프 a 변수 참조
    print(f"b: {b}")

vartest() #
print(f"a: {a}")

# def vartest2():
    # 로컬스코프에서 글로벌 스코프 변수
    # 수정을 바로 시도하는 것은 불가능하다.
    # a = a + 1  # 글로벌 스코프 a 변수 참조
    # print(f"a: {a}")

# vartest2() #

def vartest3():
    # 로컬스코프에서 글로벌 스코프 변수
    # 수정을 바로 시도하는 것은 불가능하다.
    # 아래와 같이 global 키워드로 사용할 수 있게
    # 선언해야 한다.
    global a
    a = a + 1  # 글로벌 스코프 a 변수 참조
    print(f"a: {a}")

vartest3() #
