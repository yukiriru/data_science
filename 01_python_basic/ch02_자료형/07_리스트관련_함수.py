#############################
# append
######################
a=[1,2,3]
print(type(a))
a.append([5,6]) # 리스트 확장이 아니라 마지막 요소에 값을 추가
print(a)
a=[1,2,3]
print(a)
# append 함수를 사용해서 [1,2,3,4,5] 를 만들고 싶을때
a.append(4)
a.append(5)
print(a)

##########################
# sort
##########################
a = [1,4,3,2]
print(a)
a.sort()
print(a)
b=['a','c','b']
print(b)
b.sort()
print(b)
a=['a','c','b']
a.reverse() # 배열의 순서를 뒤집는다
print(a)

a = [1,4,3,2]
a.reverse()
print(a)

# 그렇다면 내림차순 정렬은?
a = [1,4,3,2]
a.sort(reverse=True)
print(a)

##############################
# 출력 포맷 설정 및 자동화
#############################
a = [1,4,3,2]
print(f"a: {a}")
a.sort(reverse=True)
print(f"a: {a}")

############
# 리스트의 값은 변경(Mutable)가능한 속성을 가지고 있다.
a = [1,4,3,2]
print(f'a.append(5): {a.append(5)}') #자기 자신의 값을 변경만 하고 해당 변수를 반환하지 않음
print(f"a: {a}")
print(f"a[0]: {a[0]}")
a[0] = 5 # 리스트는 값을 변경 간ㅇ하다.
print(f"a[0]: {a[0]}")