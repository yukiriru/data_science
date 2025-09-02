def add_two_number():
    global result
    number1 = 10
    number2 = 20
    print("=" * 10)
    print("입력값 확인")
    print(f'number1: {number1}, number2: {number2}')
    result = number1 + number2


add_two_number()

print("="*10)
print("최종결과")
print(f"result: {result}")

add_two_number()

print("="*10)
print("최종결과")
print(f"result: {result}")