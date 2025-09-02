a= [1,2,3]
try:
    a[3]
except Exception as e:
    print(f"\런타임 에러: {e}")


print('프로그램 정상 종료')
