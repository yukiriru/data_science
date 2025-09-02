a = [1,2,3]
b = [4,5,6]
print(a + b)
c = ['a','b','c']
print(a+c) # 타입이 다른 리스트도 + 연산 가능
temp = [1,2,3,'a','b','c']
print(temp)
print(a*2) # 곱한 숫자만큼 반복

# print(a[2] + "hi") # 런타임 에러 발생

print(a[2]) #인덱스로 지정할 경우에는 해당 요소의 고유의 타입으로 반환
print(a[2:]) #슬라이싱 할 경우에는 리스트로 해당 요소를 포함하여 반환

# print(3 + "hi")
a = [1,2,3,'a','b','c']
print(a[3] + "hi")
print('a' + "hi")
print(a[3:4])
# print(a[3:4] +"hi") # 리스트와 문자열의 + 연산이므로 서로다른 타입간의 연산이다.
# 비록, 리스트의 요소가 문자열일지라도
# print(['a']+'hi')
print([1]+[2])

####################################
# 리스트의 길이 구하기

a=[1,2,3]
print(len(a))
print(len([1,2,3])) # a 변수가 할당된 값으로 치환
print(3) # len함수의 수행 결과로 치환
a[1]=4
print(a)
print("프로그램 종료")

# 리스트의 전체 값 조회 (예습)
numbers = [1,2,3,4,5]

# 열거형타입(Enumeration Type): 여러개의 값을 포함할 수 있는 타입
# 예) 문자열, list, tuple, dict
# for 개별값 in 열거형타입의값
for number in numbers:
    print(number)
# 파이썬에서 여러줄 주석은?
"""
Step1]
for number in [1,2,3,4,5]:
    print(number)
Step2]
for 1 in [1,2,3,4,5]:
    print(number)    
Step3]
for 1 in [1,2,3,4,5]:
    print(1)     
Step2]
for 2 in [1,2,3,4,5]:
    print(number)    
Step3]
for 2 in [1,2,3,4,5]:
    print(2)    
..... Step2,3이 리스트의 마지막 값이 5가 될때까지 반복      
"""
item_list = ['핸드폰','지갑','차키']
print( '차키' in item_list)
print( '지폐' in item_list)
