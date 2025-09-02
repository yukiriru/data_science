# 타입 힌트 예제
# -----------------------------------
# 타입 힌트(Type Hint)는 "이 변수나 매개변수, 반환값은 어떤 타입이 될 것"이라는
# '의도'를 코드에 표시하는 방법입니다.
# 실행 속도에는 영향을 주지 않으며, 코드의 가독성과 유지보수를 위해 사용됩니다.
# -----------------------------------

def sum_multiples_of_three(end_number: int) -> int:
    """
    1부터 end_number까지의 정수 중 3의 배수 합계를 반환한다.

    매개변수:
        end_number (int): 합계를 구할 마지막 정수 (정수 타입을 기대함)

    반환값:
        int: 3의 배수의 합계 (정수 타입으로 반환)
    """
    total_sum = 0
    for i in range(1, end_number + 1):
        if i % 3 == 0:
            total_sum += i
    return total_sum


# -----------------------------------
# [타입 힌트의 의미]
# - end_number: int   → end_number는 정수여야 한다.
# - -> int           → 이 함수는 정수를 반환해야 한다.
# -----------------------------------

# 1) 타입을 지킨 경우 - 정상 동작
result = sum_multiples_of_three(10)   # end_number = 10 (int)
print("정상 호출 결과:", result)      # 3+6+9 = 18

# 2) 타입을 어긴 경우 - 파이썬은 실행 시 타입 힌트를 강제하지 않음
# 아래 코드는 실행은 되지만, 내부에서 range("10")을 하려다 에러 발생
try:
    wrong_result = sum_multiples_of_three("10")  # 문자열을 넣음 (잘못된 타입)
except TypeError as e:
    print("잘못된 타입 사용 시 런타임 에러 발생:", e)


