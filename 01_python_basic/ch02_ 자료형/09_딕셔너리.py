l_person_info = ['홍길동','010-123-4567','1294/03/27']
#전제조건: 이름, 전화번호, 생년월일의 인덱스가 무엇인지 알고 있어야 한다.
print(f"l_person_info[0]: {l_person_info[0]}") # 이름 검색하고 싶을때
print(f"l_person_info[1]: {l_person_info[1]}") # 전화 번호 검색하고 싶을때
print(f"l_person_info[2]: {l_person_info[2]}") # 생년월일 검색하고 싶을때
d_person_info = {
        '이름':'홍길동',
        '전화번호':'010-123-4567',
        '생년월일' :'1294/03/27'
}
#d_person_info['이름']
print(f"d_person_info['이름']: {d_person_info['이름']}")
print(f"d_person_info['전화번호']: {d_person_info['전화번호']}")
print(f"d_person_info['생년월일']: {d_person_info['생년월일']}")
print(f"type(d_person_info): {type(d_person_info)}")

# dict 요소 추가 + 수정
# 딕셔너리명['키'] = 값
d_person_info['나이'] = 45
print(f"d_person_info: {d_person_info}")

d_person_info['이름'] = '홍순이'
print(f"d_person_info: {d_person_info}")
d_person_info['나이'] = 21
print(f"d_person_info: {d_person_info}")


#dict 요소 삭제
#del 딕셔너리명['키']
del d_person_info['나이']
print(f"d_person_info: {d_person_info}")

#모든 키값 조회
print(f"d_person_info.keys(): {d_person_info.keys()}")
print(f"list(d_person_info.keys()): {list(d_person_info.keys())}")

#모든 요소 삭제
d_person_info.clear()
print(f"d_person_info: {d_person_info}")

d_person_info = {
        '이름':'홍길동',
        '전화번호':'010-123-4567',
        '생년월일' :'1294/03/27'
}

print(f"d_person_info['이름']: {d_person_info['이름']}")
#dict 내장함수로 키로 매핑되는 값 가져오기
print(f"d_person_info.get('이름'): {d_person_info.get('이름')}")
# dict 요소 접근 기본 문법 vs get()
# 기본문법: 해당 키가 없으면 런타임 에러 발생
# print(f"d_person_info['주소']: {d_person_info['주소']}")
print(f"d_person_info.get('주소'): {d_person_info.get('주소')}")
print(f"d_person_info.get('주소','대구 수성구 알파시티1로 170'): {d_person_info.get('주소','대구 수성구 알파시티1로 170')}")

print("정상 종료")

# dict 전체 값 조회
print(f"d_person_info.keys(): {d_person_info.keys()}")
# 전체 키값을 개별 타임으로 조회

for key in d_person_info.keys():
    print(f"key: {key}")
    
# 전체 value 값 조회
print(f"d_person_info.values(): {d_person_info.values()}")

# 전체 value의 개별 타입으로 조회
for value in d_person_info.values():
    print(f"value: {value}")

for key in d_person_info.keys():
    print(f"d_person_info[key] : {d_person_info[key]}")

for key in d_person_info.keys():
    print(f"d_person_info.get('{key}') : {d_person_info.get(key)}")


# 전체 item(key,value) 조회
print(f"d_person_info.items(): {d_person_info.items()}")

# 개별 item 조회
for item in d_person_info.items():
    print(f"item: {item}")


"""
d_person_info = {
        '이름':'홍길동',
        '전화번호':'010-123-4567',
        '생년월일' :'1294/03/27'
}
"""

#개별 item을 key, value로 조회
print('{')
for key, value in d_person_info.items():
    print(f"{key}: {value}")
print('}')