# num1 =int(input("첫 번째 수를 입력하세요: "))
# num2 =int(input("두 번째 수를 입력하세요: "))
# print(f"두 수의 합은 {num1+num2}입니다.")
#

# num1 =int(input("정수를 입력하세요: "))
# if num1 % 2== 0 :
#     print(f"{num1}은(는) 짝수입니다.")
# else:
#     print(f"{num1}은(는) 홀수입니다.")


# num1 =int(input("첫 번째 수를 입력하세요: "))
# num2 =int(input("두 번째 수를 입력하세요: "))
# print(f' 더 큰수는 {max(num1,num2)}입니다.')

# num1 =int(input("첫 번째 수를 입력하세요: "))
# num2 =int(input("두 번째 수를 입력하세요: "))
# num3 =int(input("세 번째 수를 입력하세요: "))
# print(f'가장 큰 수는 {max(num1,num2,num3)}입니다.')

# score =int(input("점수를 입력하세요: "))
#
# if score > 90 :
#     print("학점은 A입니다")
# elif score > 80:
#     print("학점은 B입니다")
# elif score > 70:
#     print("학점은 C입니다")
# elif score > 60:
#     print("학점은 D입니다")
# else :
#     print("학점은 F입니다")

username = input("아이디를 입력하세요: ")
password = input("비밀번호를 입력하세요: ")

if (username == 'admin') and (password == 'password'):
    print("로그인에 성공했습니다.")
else:
    print("로그인에 실패했습니다.")
aa = input("주민등록번호를 입력하세요 (ex. 123456-1234567)")
if aa[7] == "1" or aa[7] == "3" :
    print("입력한 주민등록번호는 남성입니다")
elif aa[7] == "2" or aa[7] =="4" :
    print("입력한 주민등록번호는 여성입니다")
print(aa[7])