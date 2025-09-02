# 문제 5) 아이디/비밀번호 검사 결과 출력
# - 함수 형태: def print_login_result(input_username: str, input_password: str) -> None
# - 요구사항: 사전 정의된 valid_username, valid_password와 모두 일치하면 “로그인 성공”, 아니면 “로그인 실패” 출력.
# - 힌트: 논리 AND.

# 사전 정의된 유효한 계정(실습용 하드코딩)
VALID_USERNAME = "admin"
VALID_PASSWORD = "1234"

def print_login_result(input_username: str, input_password: str) -> None:
    """입력받은 아이디/비밀번호가 유효 계정과 일치하는지 검사해 결과를 출력한다."""
    if (input_username == VALID_USERNAME) and (input_password == VALID_PASSWORD):
        print("로그인 성공")
    else:
        print("로그인 실패")


if __name__ == "__main__":
    # 예시 실행
    print_login_result("admin", "1234")  # 로그인 성공
    print_login_result("admin", "wrong") # 로그인 실패
