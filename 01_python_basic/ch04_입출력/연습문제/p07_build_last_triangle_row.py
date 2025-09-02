# 문제 7) 사용자 입력으로 삼각형 높이를 받아 마지막 줄 문자열 반환
# - 함수 형태: def build_last_triangle_row() -> str
# - 요구사항: input()으로 높이 정수 입력을 받고, 그 높이에 해당하는 마지막 줄(예: 높이 5면 "*****") 문자열을 만들어 반환.
# - 힌트: '*' * height.

def build_last_triangle_row() -> str:
    """사용자에게 삼각형 높이를 입력받아 마지막 줄 문자열을 생성해 반환한다."""
    raw_height = input("삼각형 높이를 입력하세요(정수): ").strip()
    height = int(raw_height)  # 숫자 변환 (잘못 입력 시 ValueError 발생 가능)
    if height < 0:
        # 음수를 입력했을 경우 빈 문자열을 반환(간단 처리)
        return ""
    # 높이만큼 별(*)을 이어붙인 문자열이 마지막 줄
    last_row = "*" * height
    return last_row


if __name__ == "__main__":
    # 예시 실행
    result = build_last_triangle_row()
    print(f"마지막 줄: {result}")
