# 문제 6) 정수 리스트 평균 출력
# - 함수 형태: def print_average(scores: list[int]) -> None
# - 요구사항: 리스트 scores의 합과 길이로 평균을 계산해 소수 포함하여 출력.
# - 힌트: 누적 합 total_score → total_score / len(scores).

def print_average(scores: list[int]) -> None:
    """정수 리스트의 평균을 계산하여 출력한다.

    매개변수:
        scores (list[int]): 정수 점수 리스트
    """
    if len(scores) == 0:
        print("빈 리스트입니다. 평균을 계산할 수 없습니다.")
        return

    total_score = 0  # 합계를 저장할 변수
    for score_value in scores:
        total_score += score_value
    average_value = total_score / len(scores)
    print(f"평균: {average_value}")


if __name__ == "__main__":
    # 예시 실행
    print_average([70, 80, 90])  # 평균: 80.0
