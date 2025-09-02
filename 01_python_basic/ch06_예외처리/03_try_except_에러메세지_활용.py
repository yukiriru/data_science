a = [1,2,3]
try:
    a[3]
    # IndexError: list index out of range
    # 코드 실행시 발생하는 런타임에러 클래스명을 아래 except에 기술한다.
except IndexError as e:
    print(f'Index error: {e}') # IndexError 런타임 오류 발생시 수행되는 코드

print('프로그램 정상 종료')