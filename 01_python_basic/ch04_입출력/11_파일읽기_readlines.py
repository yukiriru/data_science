f = open("새파일.txt","r",encoding="utf-8")
line = f.readlines()
print(line)
f.close()