f = open("새파일.txt","r",encoding="utf-8")
# 파일 내용 전체를 통으로 한꺼번에
# 가져온다.
# 단순 조회, 복사본 만들때 유리
lines = f.read()
print(lines)
f.close()