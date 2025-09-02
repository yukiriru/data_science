# 문제 2) 세 정수 중 최댓값 반환
# - 함수 형태: def max_of_three(num_a: int, num_b: int, num_c: int) -> int
# - 요구사항: if 문만 사용해 최댓값을 찾아 반환(내장 max 사용 금지).
# - 힌트: current_max에 하나씩 비교·갱신.

def max_of_three(num_a: int, num_b: int, num_c: int) -> int:
    """세 정수 중 최댓값을 반환한다(내장 max 사용 금지).

    매개변수:
        num_a (int), num_b (int), num_c (int): 비교할 정수들

    반환값:
        int: 세 수 중 가장 큰 값
    """
    current_max = num_a  # 첫 번째 값을 현재 최댓값으로 가정
    if num_b > current_max:
        current_max = num_b  # 두 번째 값이 더 크면 교체
    if num_c > current_max:
        current_max = num_c  # 세 번째 값이 더 크면 교체
    return current_max


if __name__ == "__main__":
    # 예시 실행
    print("예시) 7, 3, 9 ->", max_of_three(7, 3, 9))  # 9
