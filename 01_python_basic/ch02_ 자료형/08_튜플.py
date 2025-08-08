t1 = () # 빈 튜퓰 초기화
print(f"t1: {t1}")
t2 = (1,) # 요소 1개일 때의 튜플
print(f"t2: {t2}")
t2 = (1)
print(f"t2: {t2}")
print(f"type(t2): {type(t2)}")
t3 = (1,2,3)
print(f"t3: {t3}")
t4 = 1,2,3
print(f"t4: {t4}")
t1 = (1,2,'a','b')
# t1[0] =7 ##
# del t1[0]  # 튜플은 Immutable 타입이라 변경이 불가하기 때문에 해당 작업 수행시 에러 발생
print(f"t1[1:]: {t1[1:]}")
print(f"t1[:1]: {t1[:1]}")



t1 = (1,2,'a','b')
t2= (3,4)
t3= t1+t2
print(f"t1: {t1}")
print(f"t2: {t2}")
print(f"t3: {t3}")
t4 =t2*3
print(f"t4: {t4}")
print(f"t2*3: {t2*3}")

# 그럼 튜플은 어떻게 정렬하지?
# STEP1] 정렬하는 내장 함수 사용
t_unsorted = (5,1,3,2,7)
print(f"t_unsorted: {t_unsorted}")
l_sorted=sorted(t_unsorted) # 정렬을 위한 내장 함수 사용, 결과는 리스트로 반환해준다
print(f"l_sorted: {l_sorted}")
# STEP2] 다시 튜플로 반환하려면?
t_sorted = tuple(l_sorted)
print(f"t_sorted: {t_sorted}")

#튜플을 개별 타입을 받는 방법
t6 = ('나이', 45)
print(f"t6: {t6}")
age_key, age_val =('나이', 45)
print(f"age_key: {age_key}, age_val: {age_val}")
## print(f"age_key: type({age_key}), age_val: type({age_val})")