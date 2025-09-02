# 문제 1) 1부터 n까지 3의 배수 합 구하기
# - 함수 형태: def sum_multiples_of_three(end_number: int) -> int
# - 요구사항: 1부터 end_number까지의 정수 중 3의 배수 합계를 계산해 정수로 반환.
# - 힌트: 누적 변수 total_sum 사용.

def sum_multiples_of_three(end_number: int) -> int:
    """1부터 end_number까지의 정수 중 3의 배수 합계를 반환한다.

    매개변수:
        end_number (int): 합계를 구할 마지막 정수(포함).

    반환값:
        int: 3의 배수의 합계.
    """
    total_sum = 0  # 누적합을 저장할 변수
    for current_number in range(1, end_number + 1):
        if current_number % 3 == 0:  # 3의 배수인지 검사
            total_sum += current_number
    return total_sum


if __name__ == "__main__":
    # 예시 실행
    print("예시) end_number=10 ->", sum_multiples_of_three(10))  # 3+6+9 = 18
