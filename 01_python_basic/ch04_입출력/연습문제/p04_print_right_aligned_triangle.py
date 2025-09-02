# 문제 4) 오른쪽 정렬 직각삼각형 별 찍기
# - 함수 형태: def print_right_aligned_triangle(height: int) -> None
# - 요구사항: 높이 height만큼 공백+별 조합으로 오른쪽 정렬 삼각형 출력.
# - 힌트: blank_count = height - row, '*' * row.

def print_right_aligned_triangle(height: int) -> None:
    """오른쪽 정렬 직각삼각형을 출력한다.

    매개변수:
        height (int): 삼각형 높이(줄 수)
    """
    for row_index in range(1, height + 1):
        blank_count = height - row_index       # 왼쪽 공백 개수
        star_count = row_index                 # 별의 개수
        line = (" " * blank_count) + ("*" * star_count)
        print(line)


if __name__ == "__main__":
    # 예시 실행
    print_right_aligned_triangle(5)
