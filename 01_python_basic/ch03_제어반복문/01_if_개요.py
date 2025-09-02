# if [리터럴값, 표현식, 변수] :
#   명령문1
#   명령문2
# else:
#   명령문3
#   명령문4
if True: # 조건에 리터럴 사용
    print("True일 때 실행")
else:
    print("False 일때 수행")

if False:
    print("True일 때 실행")
else:
    print("False 일때 수행")

if False:
    print("True일 때 실행")
else:
    print("False 일때 수행")
   # print("else문 종료") #들여쓰기를 맞추어야 한다

## if 조건: 변수인 경우
# money = True
money = False
if money:
    print("과자를 사라")
else:
    print("굶어라")

print("프로그램 종료")

## if 조건: 표현식
money = 7000 # 내가 가진돈

if money >= 7000: # 여기서 7000은 식당에 갈수 있는 최소 금액
    print("식당 갈 수 있어요")
else:
    print("굶거나 편의점 가세요")

money = 6000 # 내가 가진돈
MINIMUM_REST_FEE = 7000 # 상수를 표현, 파이썬에서는 대문자로 표시
if money >= MINIMUM_REST_FEE: # 여기서 7000은 식당에 갈수 있는 최소 금액
    print("식당 갈 수 있어요")
else:
    print("굶거나 편의점 가세요")

money = 2000
card = False
if money >= MINIMUM_REST_FEE or card is True:
    print("식당 갈 수 있어요")
else:
    print("굶거나 편의점 가세요")

card = False
if card is True:
  print("식당 갈 수 있어요")

if card is False: # 카드가 없는 경우
    print("굶거나 편의점 가세요")

if not card: # 카드가 없는 것이 아니라면
    print("식당에 갈 수 있어요")

card = True
if not card: # 카드가 있는 것이 아니라면
    print("굶거나 편의점 가세요")

# 식당 방문 처리 요구사항
# 1.아래 경우는 식당 방문
#  1.1 주머니에 돈이 7000원 이상인 경우
#  1.2. 주머니에 신용카드가 있는 경우
# 식당 방문 가능한 경우는 추후 메세지 처리 가능
# 2. 식당 방문할 수 없는 상황은 설계회의후 결정

# Step1] 알고리즘 뼈대 설계
my_money = 2000
card = False
MINIMUM_REST_FEE = 7000
if my_money >= MINIMUM_REST_FEE:
    pass
elif card is True:
    pass
else:
    pass

# 식당 방문 처리 요구사항 상세화
# 1.아래 경우는 식당 방문
#  1.1 주머니에 돈이 7000원 이상인 경우
#  1.2. 주머니에 신용카드가 있는 경우
# 식당 방문 가능한 경우는 아래 메세지 처리 가능
# '식당에 방문할 수 있습니다.'
# 2. 식당 방문할 수 없는 상황은 아래 메세지 처리
# '굶으세요'

# Step2] 알고리즘 구현
my_money = 2000
card = False
MINIMUM_REST_FEE = 7000
if my_money >= MINIMUM_REST_FEE:
    print('식당에 방문할 수 있습니다.')
elif card is True:
    print('식당에 방문할 수 있습니다.')
else:
    print('굶으세요')

# Step3] 최적화
if my_money >= MINIMUM_REST_FEE or card is True:
    print('식당에 방문할 수 있습니다.')
else:
    print('굶으세요')

# A조건 B조건: TC1(T,T), TC2(T,F), TC3(F,T), TC4(F,F)
#TC1(T,T)
my_money = 5000
card = True
# Step4] 제어문 검증
if my_money >= MINIMUM_REST_FEE or card is True:
    print('식당에 방문할 수 있습니다.')
else:
    print('굶으세요')

# in연산을 통해서 복수개의 or조건 간소화 하기
pocket = ['만원지폐','신용카드','상품권']

if '차키' in pocket:
    print('식당 갈 수 있습니다.')
else:
    print('굶으세요')

score = 50
message=''
if score >= 70:
    message = "success"
else:
    message = "fail"

print(f"message: {message}")

message = "success" if score >= 70 else "fail"
print(f"message: {message}")