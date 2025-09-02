# 1. 매개변수: X, 리턴: X
# 모든 처리를 위임
# 파라메터(입력), 리턴(출력)
def add_no_param_no_return():
    # 핵심 로직을 수행하기 위한 입력값
    num1 = 3
    num2 = 5

    # 핵심 로직
    total = num1 + num2

    # 사후 처리 로직
    print("1) 매개변수X, 리턴X:", total)

# 2. 매개변수: O, 리턴: X
def add_with_param_no_return(num1, num2):
    total = num1 + num2
    print("2) 매개변수O, 리턴X:", total)

# 3. 매개변수: X, 리턴: O
def add_no_param_with_return():
    num1 = 7
    num2 = 8
    total = num1 + num2
    return total

# 4. 매개변수: O, 리턴: O
def add_with_param_with_return(num1, num2):
    return num1 + num2


# 함수 호출 예시

# 모든 기능 위임
add_no_param_no_return()

# 기능을 수행하기 위한 입력값만 전달
add_with_param_no_return(10, 20)

# 입력은 신경쓰지 않고 사후 처리를 호출한 쪽에서 한다.
print("3) 매개변수X, 리턴O:", add_no_param_with_return())

# 비즈니스 로직만 활용한다. 입력과 사후처리를 호출하는 파트에서
# 담당한다.
print("4) 매개변수O, 리턴O:", add_with_param_with_return(15, 25))
