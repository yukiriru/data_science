# q1_functions_args_return.py

def example1(num1, num2):
    return num1 + num2

def example2(num):
    if num % 2 == 0:
        return f"{num}은(는) 짝수입니다."
    else:
        return f"{num}은(는) 홀수입니다."

def example3(num1, num2):
    if num1 > num2:
        return f"더 큰 수는 {num1}입니다."
    elif num1 < num2:
        return f"더 큰 수는 {num2}입니다."
    else:
        return "두 수는 같습니다."

def example4(num1, num2, num3):
    max_num = num1
    if num2 > max_num:
        max_num = num2
    if num3 > max_num:
        max_num = num3
    return f"가장 큰 수는 {max_num}입니다."

def example5(score):
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return f"학점은 {grade}입니다."

def example6(username, password):
    if (username == 'admin') and (password == 'password'):
        return "로그인에 성공했습니다."
    else:
        return "로그인에 실패했습니다."

def example7(registration_number):
    gender_digit = int(registration_number[7])
    if gender_digit == 1:
        gender = "남성"
    else:
        gender = "여성"
    return f"입력한 주민등록번호는 {gender}입니다."


# 실행 시 바로 호출
num1 = int(input("첫 번째 수를 입력하세요: "))
num2 = int(input("두 번째 수를 입력하세요: "))
print(f"두 수의 합은 {example1(num1, num2)}입니다.")

num = int(input("정수를 입력하세요: "))
print(example2(num))

num1 = int(input("첫 번째 수를 입력하세요: "))
num2 = int(input("두 번째 수를 입력하세요: "))
print(example3(num1, num2))

num1 = int(input("첫 번째 숫자를 입력하세요: "))
num2 = int(input("두 번째 숫자를 입력하세요: "))
num3 = int(input("세 번째 숫자를 입력하세요: "))
print(example4(num1, num2, num3))

score = int(input("점수를 입력하세요: "))
print(example5(score))

username = input("아이디를 입력하세요: ")
password = input("비밀번호를 입력하세요: ")
print(example6(username, password))

registration_number = input("주민등록번호를 입력하세요 (ex. 123456-1234567): ")
print(example7(registration_number))
