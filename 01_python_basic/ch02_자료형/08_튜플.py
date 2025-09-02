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
print(f"t1: {t1}") # 튜플 전체 조회
print(f"t1[0]: {t1[0]}") # 튜플 요소 조회: 인덱스로 조회, 리스트 문법과 똑같다.
print(f"t1[1]: {t1[1]}")
# t1[0] = 7 # 튜플은 Immutable 타입이라 변경(수정)이 불가하기 때문에 해당 작업 수행시 에러 발생
# del t1[0]  # 튜플은 Immutable 타입이라 변경(삭제)이 불가하기 때문에 해당 작업 수행시 에러 발생
print(f"t1[:1]: {t1[:1]}")
print(f"t1[1:]: {t1[1:]}")

###########################
# 튜플 연산 (더하기, 곱하기
t1 = (1,2,'a','b')
t2 = (3,4)
t3 = t1 + t2
print(f"t1: {t1}")
print(f"t2: {t2}")
print(f"t3: {t3}")
t4 = t2 * 3
print(f"t4: {t4}")
print(f"t2*3: {t2*3}")
print(f"len(t1): {len(t1)}")

# 그럼 튜퓰은 어떻게 정렬하지?
# Step1] 정렬하는 내장 함수 사용
t_unsorted = (5,1,3,2,7)
print(f"t_unsorted: {t_unsorted}")
l_sorted = sorted(t_unsorted) # 정렬을 위한 내장 함수 사용, 결과는 리스트로 반환해준다.
print(f"l_sorted: {l_sorted}")
# Step2] 다시 튜플로 변환하려면?
t_sorted = tuple(l_sorted) # 열거형 자료형을 튜플로 변환해주는 함수
print(f"t_sorted: {t_sorted}")
# 추가나 삭제를 하고 싶다면
t5 = (1,2,3,4,5)
print(f"t5: {t5}")
# 6을 추가하고 싶다면
t5 = (1,2,3,4,5,6)
print(f"t5: {t5}")
# 5,6을 빼고 싶다면
t5 = (1,2,3,4)
print(f"t5: {t5}")

# 튜플을 개별 타입을 받는 방법
t6 = ('나이', 45) # 튜플을 튜플로 대입
print(f"t6: {t6}")
age_key, age_val = ('나이', 45)
print(f"age_key: {age_key}, age_val: {age_val}")
print(f'type(age_key): {type(age_key)}, type(age_val): {type(age_val)}')
