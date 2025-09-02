f = open("새파일.txt","r",encoding="utf-8")
lines = f.readlines()

# 줄단위 분석시 유리하다.
for line in lines:
    # 현재 방식으로 출력하면 줄바꿈이 2번 일어난다.
    # print(line)
    # print(line.strip()) # 문자열 끝에 \n을 제거
    print(line, end='') # print옵션을 사용해 원본 그대로 출력
f.close()