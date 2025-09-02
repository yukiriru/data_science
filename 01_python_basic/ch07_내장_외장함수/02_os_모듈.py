import os

# 1. 디렉토리 만들기
DIR_NAME = "test_dir"
if not os.path.exists(DIR_NAME):
    os.makedirs(DIR_NAME)

# 2. 디렉토리명 수정
# os.rename("test_dir", "test_dir2")

# 3. 파일 삭제
# os.remove("test_dir2\new_file.txt")
os.remove("test_dir2/new_file.txt")
