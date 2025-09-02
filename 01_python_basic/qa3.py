# age  = int(input("나이를 입력하세요: "))
# if age >=66 :
#     fee ="무료"
# elif age >=19 :
#     fee ="5000원"
# elif age >=14 :
#     fee ="3000원"
# elif age >=4 :
#     fee ="2000원"
# else:  fee ="무료"
# print(f'요금은 {fee}입니다')

# age  = int(input("나이를 입력하세요: "))
# if age >=66 :
#     fee ="무료"
#     a = "노인"
# elif age >=19 :
#     fee ="5000원"
#     a = "성인"
# elif age >=14 :
#     fee ="3000원"
#     a = "청소년"
# elif age >=4 :
#     fee ="2000원"
#     a = "어린이"
# else:
#     fee ="무료"
#     a ="유아"
# print(f'귀하는 {a} 등급이며 요금은 {fee}입니다')

# age  = int(input("나이를 입력하세요: "))
# if age >=66 :
#     fee = 0
#     a = "노인"
# elif age >=19 :
#     fee =5000
#     a = "성인"
# elif age >=14 :
#     fee =3000
#     a = "청소년"
# elif age >=4 :
#     fee =2000
#     a = "어린이"
# else:
#     fee =0
#     a ="유아"
# print(f'귀하는 {a} 등급이며 요금은 {fee}원입니다')
#
# c =input("요금 유형을 선택하세요. (1: 현금, 2: 공원 전용 신용 카드)")
# if c == "1" :`
#     b = int(input("요금을 입력하세요. "))
#     if b < int(fee):
#         print(f"{fee-b}원이 모자랍니다. 입력 하신 {b}원을 반환합니다.")
#     elif b == int(fee) :
#         print("감사합니다. 티켓을 발행합니다.")
#     else :
#         print(f"감사합니다. 티켓을 발행하고 거스름돈 {b-fee}원을 반환 합니다.")
# elif c == "2" :
#     if age > 66 :
#         print("무료 대상입니다. 요금은 0원 입니다.")
#         exit()
#     if age > 60 :
#         fee *= 0.85
#     else :
#         fee *= 0.9
#     print(f"공원 전용카드로 {int(fee)}원 결제되었습니다. 티켓을 발행합니다.")

cus_num =0 #고객수
event_ticket = 3
discount_ticket =5
while(True):
    age  = int(input("나이를 입력하세요: "))
    if age >=66 :
        fee = 0
        grade = "노인"    # 연습문제에서 변수명은 의미있게
    elif age >=19 :
        fee =5000
        grade = "성인"
    elif age >=14 :
        fee =3000
        grade = "청소년"
    elif age >=4 :
        fee =2000
        grade = "어린이"
    else:
        fee =0
        grade ="유아"
    print(f'귀하는 {grade} 등급이며 요금은 {fee}원입니다')
    if age > 66 or age < 4:
        print("무료 대상입니다. 요금은 0원 입니다.")# 프로그램 종료에 대한 요구사항없음
    else :
        fee_type =input("요금 유형을 선택하세요. (1: 현금, 2: 공원 전용 신용 카드)")
        if fee_type == "1" :
            fee_b = int(input("요금을 입력하세요. "))
            if fee_b < int(fee):
                print(f"{fee-fee_b}원이 모자랍니다. 입력 하신 {fee_b}원을 반환합니다.")
                continue
            elif fee_b == int(fee) :
                cus_num += 1
                print("감사합니다. 티켓을 발행합니다.")
            else :
                print(f"감사합니다. 티켓을 발행하고 거스름돈 {fee_b-fee}원을 반환 합니다.")
                cus_num += 1
        elif fee_type == "2" :
            if age > 60 :
                fee *= 0.85
            else :
                fee *= 0.9
            print(f"공원 전용카드로 {int(fee)}원 결제되었습니다. 티켓을 발행합니다.")
            cus_num += 1

        # 이벤트 티켓
        cus_num +=1
        print(cus_num)
        if (cus_num  % 7 == 0) and event_ticket !=0 :
            print(f"축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료티켓 {event_ticket}장")
            event_ticket -= 1
        if cus_num % 4 == 0 and discount_ticket !=0 :
            print(f"축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 {discount_ticket}장")
            discount_ticket -= 1