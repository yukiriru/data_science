# 빈 set 변수로 생성하기
s = set()
print(f"s: {s}")
# set 자료형: 유일한 데이터 목록을 식별할 때 사용하는 자료형
s1 = set([1,2,3,5,8,2,3,3,1,8,8])
print(f"s1: {s1}")

# 문자열내에 중복되는 알파벳을 제거하여 유일한 목록으로 제공
s2 = set("Python is powerful languages")
print(f"s2: {s2}")

s1 = set([1,2,3])
print(f"list(s1): {list(s1)}")
print(f"tuple(s1): {tuple(s1)}")

# 리스트에 존재하는 요소중 중복되는 요소를 제거하여 유일한 목록으로 제공
s3 = set(["Python", "Java", "C++", "Java"])
print(f"list(s3): {list(s3)}")

# 교집합, 합집합, 차집합
set1 = {1, 2, 3, 4 }
set2 = {3, 4, 5, 6 }
# 교집합
print(f"set1 & set2: {set1 & set2}")
# 합집합
print(f"set1 | set2: {set1 | set2}")
# 차집합
print(f"set1 - set2: {set1 - set2}")
print(f"set2 - set1: {set1 - set2}")
# 대칭 차집합: set1, set2에만 있는 값
print(f"set1 ^ set2: {set1 ^ set2}")

# 집합 자료형 관련 함수
set = {1, 2, 3, 4 }
set.add(5)
print(f"set: {set}")
set.update([6,7,8])
print(f"set: {set}")
set.remove(6)
print(f"set: {set}")