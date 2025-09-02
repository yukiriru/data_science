a= [1,2,3]
try:
    a[3]
except IndexError as e:
    print(f"Index error: {e}")


print('프로그램 정상 종료')
