a=[1,2,3,4,5]
print(f"a.index(4): {a.index(4)}")

b=['k','l','m','n']
# print(f"b.index(3): {b.index(3)}") # 3이 리스트 b에 없기 때문에 에러 발생
print(f"b.index('l'): {b.index('l')}") # 리스트에 있는 요소로 검색해야 한다.

a = [1,2,3]
# print(f"a.insert(0,4): {a.insert(0,4)}")
a.insert(0,4)
print(f"a: {a}")
a.insert(3,5)
print(f"a: {a}")
del a[4] # del 을 이용한 리스트 요소 삭제
print(f"a: {a}")
del a[0]
print(f"a: {a}")