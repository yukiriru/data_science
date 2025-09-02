# 파일 핸들이 닫히지 않는 상태에서 시스템 리소스가 계속 쌓일수 있다.
# while True:
#     f = open("새파일.txt",'w', encoding='utf-8')
#     f.write('Life is too short, you need python')

# with 이하의 명령문 블록 수행 종료후 파일 핸들이 자동으로 닫힌다.
with open("새파일.txt",'w',encoding='utf-8') as f:
    # 파일 관련된 로직
    print('새파일.txt를 열었습니다.')
    f.write('Life is too short, you need python')
    print('메세지를 작성했습니다.')