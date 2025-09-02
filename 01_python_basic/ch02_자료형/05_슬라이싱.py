str = "12345"
print(str[0:2])
list1 = [1, 2, 3, 4, 5]
print(list1[0:2])
print(list1[:2]) # 시작 인덱스 생략은 0과 동일
print(list1[2:])

# 중첩 리스트 슬라이싱
a = [
    1,
    2,
    3,
    ['a','b','c'], # a[3] : 리스트(['a','b','c'])도 결국 a[3]의 요소일 뿐이다.
    4,
    5
]
print(a[3])
print(a[3][1]) # print(['a','b','c'][1])
print(a[2:5])
print(a[3][:2])
temp = ['a','b','c']
print(temp[1])
print(['a','b','c'][1])
print(['a','b','c'][:1]) #슬라이싱 후 원래 타입으로 반환
int_list = [1,2,3,4,5]
print(int_list[:2])
