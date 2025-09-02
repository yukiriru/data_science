# 문제 9) 1부터 LIMIT까지 정수 출력
# - 함수 형태: def print_numbers_1_to_limit() -> None
# - 요구사항: 상수 LIMIT를 정의하고 1부터 LIMIT까지 한 줄에 하나씩 출력.
# - 힌트: for number in range(1, LIMIT + 1).

LIMIT = 20  # 요구사항의 상수. 필요에 따라 값만 바꾸면 동작이 달라진다.

def print_numbers_1_to_limit() -> None:
    """1부터 LIMIT까지의 정수를 줄바꿈하며 출력한다."""
    for number in range(1, LIMIT + 1):
        print(number)


if __name__ == "__main__":
    # 예시 실행
    print_numbers_1_to_limit()
