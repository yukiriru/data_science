# main.py
# 개발자 B가 개발
import util  # 여기서 util.py가 로드됨

print("main.py 실행 시작")
result = util.add_numbers(10, 20)
print("10 + 20 =", result)
print("main.py 실행 끝")