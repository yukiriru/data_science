# 일반 함수로 두 수를 더하는 경우
def add_normal(x, y):
    return x + y

print(f"add_normal(3,5): {add_normal(3,5)}")

# 람다 함수로 처리
# case1] 간단한 로직을 처리하기 위한 용도
# case2] 함수의 동작방식을 결정하기 위한 다른 함수의 인자로 활용
# lambda 매개변수:표현식, 리턴

# case1 예
add_lambda = lambda x, y: x + y
print(f"add_lambda(3,5): {add_lambda(3,5)}")

# case2 예
# filter
numbers = [1,2,3,4,5,6,7,8,9]
# filter(동작방식구현함수, 데이터)
# 동작방식구현함수는 필터링하는 조건을 True로 리턴해주어야 한다.
# 짝수로 필터링하는 경우
lambda x: x%2 == 0
print(f"numbers: {numbers}")
even_list = list(filter( lambda x: x%2==0 , numbers ))
print(f"even_list: {even_list}")

