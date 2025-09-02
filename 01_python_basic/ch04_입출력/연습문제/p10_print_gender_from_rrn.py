# 문제 10) 주민등록번호 앞/뒤를 입력받아 성별 출력
# - 함수 형태: def print_gender_from_rrn() -> None
# - 요구사항: input()으로 “######-#######” 형태 문자열을 받아,
#             하이픈 뒤 첫 자리(1/3 남성, 2/4 여성 등 기준)는 그대로 두고
#             단순화해서 1이면 남성, 아니면 여성 규칙으로 출력.
# - 힌트: gender_digit = int(rrn[7]), if-else.

def print_gender_from_rrn() -> None:
    """주민등록번호 형식 문자열에서 성별을 판별해 출력한다.(단순 규칙: 1이면 남성, 나머지는 여성)"""
    rrn = input("주민등록번호를 입력하세요(예: 000000-0000000): ").strip()

    # 최소 형식 검사: 길이와 하이픈 위치 확인
    if len(rrn) != 14 or rrn[6] != '-':
        print("형식이 올바르지 않습니다.")
        return

    # 문제 요구에 따라 매우 단순화된 규칙을 적용
    try:
        gender_digit = int(rrn[7])  # 하이픈 뒤 첫 자리
    except ValueError:
        print("형식이 올바르지 않습니다.")
        return

    if gender_digit == 1:
        print("남성")
    else:
        print("여성")


if __name__ == "__main__":
    # 예시 실행
    print_gender_from_rrn()
