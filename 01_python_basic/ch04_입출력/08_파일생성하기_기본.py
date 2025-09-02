# f = open("새파일.txt","w")
# 실행후 재 실행하면 기존 파일을 Overwrite한다.
f = open("smokeTest\새파일.txt","w") # 상대경로에 생성
# 주의사항] 파일경로에 \하나는 이스케이프문자 처리하기때문에
# \n 같은 경우 특수문자로 처리된다.
# f = open("smokeTest\new_file.txt","w") # 상대경로에 생성
print('\\') # \\는 백슬래시 문자 자체를 처리
f = open("smokeTest\\new_file.txt","w") # 상대경로에 생성
f.close()

# 절대 경로 처리방식
f = open("D:\\Project\\3_DataScience\\01_python_basic\\ch04_입출력\\smokeTest\\new_file.txt","w")
f.close()