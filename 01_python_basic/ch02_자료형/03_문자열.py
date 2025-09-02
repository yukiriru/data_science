# 큰따옴표로 양쪽 둘러싸기
str1 = "Hello World"
print(str1)

# 작은따옴표로 양쪽 둘러싸기
str1 = 'Hello World'
print(str1)
# 큰따옴표 3개를 연속으로 써서 양쪽 둘러싸기
str1 = """Hello World"""
print(str1)
# 작은따옴표 3개를 연속으로 써서 양쪽 둘러싸기
str1 = '''Hello World'''
print(str1)

# 큰따옴표를 사용해야만 하는 예
str1 = "Python's favorite food is perl"
print(str1)

# 'Python'까지 문자열로 인식하고 나머지는
# 문자열을 지정하는 문법을 사용하지 않아 에러
# 문장중에 소유격을 사용하는 ' 작은 따옴표 사용시 문제
# str1 = 'Python's favorite food is perl'
print(str1)

# 작은 따옴표를 사용해야만 하는 예
# ""인용구를 사용하는 문장 사용시 문제
# str1 = "Python is very easy." he says.
str1 = '"Python is very easy." he says.'
print(str1)

# 역슬래시를 사용해서
# 작은따옴표와 큰따옴표를 문자열에 포함하기
# 문자열 타입을 지정하기 위해서 작은 따옴표나 큰따옴표
# 사용시 문장에서 ',"이 사용될 지 예측하기 어려울경우
food = 'Python\'s favorite food is perl'
print(food)
# str1= '"Python\'s favorite food is perl" he says'
str1= "\"Python\'s favorite food is perl\" he says"

# 큰따옴표나 작은따옴표 3개를 사용해야 하는 경우
# 작은따옴표, 큰따옴표만 사용시 멀티라인 정의할 경우 에러발생
# str1= "Life is too short
# You need python
# "

str1= """Life is too short
You need python
"""
print(str1)

str1= '''Life is too short
You need python
'''
print(str1)

# 이스케이프 코드
multiline = "Life is too short\nYou need python"
print(multiline)

score_info="""
국어 영어 수학
100  8   88
"""
print(score_info)
score_info="""
국어\t영어\t수학
100\t8\t88
"""
print(score_info)

##################################
# 문자열은 변경이 불가능(Immutable)한 속성을 가지고 있다.

str1 = "Life is too short"
print(f"str1: {str1}")
print(f"str1[0]: {str1[0]}")
# str1[0]='N' # 변경 불가능하기 때문에 에러 발생
# str1.replace("Life", "Your leg")
# Immutalbe 한 타입의 멤버 메소드는 자기 자신을 변경할 수 없기때문에
# 변경된 값을 반환하는 특징을 가지고 있다.
print(f'str1.replace("Life", "Your leg"): {str1.replace("Life", "Your leg")}')
print(f"str1: {str1}")

# 문자열 타입이 변경 가능하다고 착각하는 이유
str1 = str1.replace("Life", "Your leg")
print(f"str1: {str1}")