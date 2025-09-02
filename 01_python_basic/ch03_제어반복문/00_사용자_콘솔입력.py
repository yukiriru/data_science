# print("텍스트를 입력하세요: ") # print함수는 마지막 문자에 \n 추가
# text1 = input() # 사용자 콘솔화면의 입력을 텍스트로 입력받는다.
# print(f"text1: {text1}")
# print("="*20)

# int 숫자 입력시
# print("정수를 입력하세요: ", end='')
# text2 = input() # 주의사항] 사용자 입력은 무조건 텍스트 타입이다.
# print(f"text2: {text2}, type(text2): {type(text2)}")
# if int(text2) % 2 == 0: # 아래와 같이 입력한 수가 숫자라면 형변환을 해줘야 한다.
#     print("짝수입니다")
# else:
#     print("홀수입니다.")
# print("="*20)

# 실수(float) 인 경우
# text3 = input("실수를 입력하세요: ")
# print(f"text3: {text3}, type(text3): {type(text3)}")
# f_value = float(text3)
# print(f": {f_value}, type(f_value): {type(f_value)}")

# 블린타입
# text4 = input("True/False를 입력하세요: ")
# print(f"text4: {text4}, type(text4): {type(text4)}")
# b_value = bool(text4)
# print(f": {b_value}, type(b_value): {type(b_value)}")

answer = input("승인여부 입력하세요(예:1, 아니오:2): ")
if answer == "1": # 파이썬에서는 문자열 비교를 == 로 할 수 있다.
    print("승인")
elif answer == "2":
    print("미승인")
else:
    print("올바른 값을 입력하세요.")
