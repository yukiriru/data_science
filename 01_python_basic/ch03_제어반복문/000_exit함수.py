answer = input("양수를 입력하세요 (종료는 q):  ")

if answer == "q":
    print('프로그램 종료합니다.')
    exit() # 강제로 프로그램 정상 종료시킴

number = int(answer)

print(f'입력하신 숫자는 {number} 입니다.')
print(f'{number} * {number} = {number*number}')