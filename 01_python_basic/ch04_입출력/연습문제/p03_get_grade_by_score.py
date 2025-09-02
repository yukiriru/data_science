# 문제 3) 점수에 따른 학점 문자 반환
# - 함수 형태: def get_grade_by_score(score: int) -> str
# - 요구사항: 90↑ A, 80↑ B, 70↑ C, 60↑ D, 그 외 F 반환.
# - 힌트: elif 사다리 구조.

def get_grade_by_score(score: int) -> str:
    """점수를 받아 학점(A/B/C/D/F)을 반환한다.

    매개변수:
        score (int): 0~100 범위의 점수

    반환값:
        str: 학점 문자
    """
    # 점수 범위에 따라 순차적으로 조건을 검사한다.
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


if __name__ == "__main__":
    # 예시 실행
    for s in (95, 84, 73, 62, 51):
        print(f"점수 {s} -> 학점 {get_grade_by_score(s)}")
