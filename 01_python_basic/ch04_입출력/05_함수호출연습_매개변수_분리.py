# q1_functions_args.py

def example1(num1, num2):
    total = num1 + num2
    print(f"두 수의 합은 {total}입니다.")

def example2(num):
    if num % 2 == 0:
        print(num, "은(는) 짝수입니다.")
    else:
        print(num, "은(는) 홀수입니다.")

def example3(num1, num2):
    if num1 > num2:
        maximum = num1
    elif num1 < num2:
        maximum = num2
    else:
        print("두 수는 같습니다.")
        return
    print(f"더 큰 수는 {maximum}입니다.")

def example4(num1, num2, num3):
    max_num = num1
    if num2 > max_num:
        max_num = num2
    if num3 > max_num:
        max_num = num3
    print("가장 큰 수는", max_num, "입니다.")

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
    print("학점은", grade, "입니다.")

def example6(username, password):
    if (username == 'admin') and (password == 'password'):
        print("로그인에 성공했습니다.")
    else:
        print("로그인에 실패했습니다.")

def example7(registration_number):
    gender_digit = int(registration_number[7])
    if gender_digit == 1:
        gender = "남성"
    else:
        gender = "여성"
    print(f"입력한 주민등록번호는 {gender}입니다.")

# 함수 호출부

# 1. 두 수의 합 구하기
example1(10, 20)  # 두 수의 합은 30입니다.

# 2. 짝수/홀수 판별
example2(7)       # 7 은(는) 홀수입니다.
example2(8)       # 8 은(는) 짝수입니다.

# 3. 두 수 중 큰 수 찾기
example3(15, 20)  # 더 큰 수는 20입니다.
example3(10, 10)  # 두 수는 같습니다.

# 4. 세 수 중 가장 큰 수 찾기
example4(5, 9, 3) # 가장 큰 수는 9 입니다.

# 5. 점수에 따른 학점 출력
example5(95)      # 학점은 A 입니다.
example5(72)      # 학점은 C 입니다.

# 6. 로그인 시도
example6('admin', 'password') # 로그인에 성공했습니다.
example6('user', '1234')      # 로그인에 실패했습니다.

# 7. 주민등록번호로 성별 판별
example7('990101-1234567')    # 입력한 주민등록번호는 남성입니다.
example7('050505-2234567')    # 입력한 주민등록번호는 여성입니다.