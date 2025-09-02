# 문제 8) 사용자 입력 세 수의 최댓값 반환
# - 함수 형태: def input_three_and_get_max() -> int
# - 요구사항: input()으로 정수 3개를 받고 if 비교로 최댓값을 찾아 반환.
# - 힌트: 비교 갱신 패턴 재사용.

def input_three_and_get_max() -> int:
    """사용자에게 정수 3개를 입력받아 최댓값을 계산하여 반환한다."""
    raw_a = input("첫 번째 정수를 입력하세요: ").strip()
    raw_b = input("두 번째 정수를 입력하세요: ").strip()
    raw_c = input("세 번째 정수를 입력하세요: ").strip()

    num_a = int(raw_a)
    num_b = int(raw_b)
    num_c = int(raw_c)

    # if 비교로 직접 최댓값 찾기
    current_max = num_a
    if num_b > current_max:
        current_max = num_b
    if num_c > current_max:
        current_max = num_c

    return current_max


if __name__ == "__main__":
    # 예시 실행
    max_value = input_three_and_get_max()
    print(f"최댓값: {max_value}")
