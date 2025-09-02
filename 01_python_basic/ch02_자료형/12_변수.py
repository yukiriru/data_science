#####################################
# 변경 불가능한 타입(Immutalbe)의 대입연산시 카피가 일어난다.
# 예) int, float, str, tuple등
a = 1
print(f"a: {a}, id(a) = {id(a)}")

b = a
print(f"b: {b}, id(b) = {id(b)}")

# 새로운 주소에 값을 할당한다.
a = 2
print(f"a: {a}, id(a) = {id(a)}")
print(f"b: {b}, id(b) = {id(b)}")


##################################
# 변경가능한(Mutalbe) 타입의 대입연산은 참조가 일어난다.
# 예) list, set, dict등
a = [1,2,3]
b = a
print(f"a: {a}, id(a) = {id(a)}")
print(f"b: {b}, id(b) = {id(b)}")
a[1] = 4
print(f"a: {a}, id(a) = {id(a)}")
print(f"b: {b}, id(b) = {id(b)}")
b[2] = 9
print(f"a: {a}, id(a) = {id(a)}")
print(f"b: {b}, id(b) = {id(b)}")

###########################
# Immutable타입의 카피

# 슬라이싱을 통한 카피
a = [1,2,3]
b = a[:]
print(f"a: {a}, id(a) = {id(a)}")
print(f"b: {b}, id(b) = {id(b)}")
a[1] = 4
print(f"a: {a}, id(a) = {id(a)}")
print(f"b: {b}, id(b) = {id(b)}")

# copy함수를 통한 복제
from copy import copy
a = [1,2,3]
b = copy(a)
print(f"a: {a}, id(a) = {id(a)}")
print(f"b: {b}, id(b) = {id(b)}")
a[1] = 4
print(f"a: {a}, id(a) = {id(a)}")
print(f"b: {b}, id(b) = {id(b)}")