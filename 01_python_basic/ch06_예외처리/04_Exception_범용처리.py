a = [1,2,3]
try:
    # a[3]
    4/0
except Exception as e: # 모든 유형의 예외를 잡아낸다.
    print(f'런타임에러: {e}')

print('프로그램 정상 종료')