# util.py로 개발되는 것을 가정
# 개발자 A가 개발

def add_numbers(a, b):
    """두 수의 합을 반환"""
    return a + b

# 함수 테스트 코드 (메인 가드 없이 작성)
# 아래와 같이 코드 작성시 외부에서 import할 경우
# 테스트 코드가 수행된다.
# 배포환경에서는 절대 이런 테스트 코드가 있으면 안된다.
# print("util.py 내부 테스트 시작")
# print("3 + 5 =", add_numbers(3, 5))
# print("util.py 내부 테스트 끝")

# 위와 같이 주석처리하거나 삭제하지 않기 위해서
# 아래와 같은 메인 가드 처리를 한다

if __name__ == "__main__":
    print("util.py 내부 테스트 시작")
    print("3 + 5 =", add_numbers(3, 5))
    print("util.py 내부 테스트 끝")