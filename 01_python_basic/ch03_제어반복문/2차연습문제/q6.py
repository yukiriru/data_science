height = int(input("삼각형의 높이를 입력하세요: "))

for start_count in range(1, height + 1):
    blank_count = height - start_count
    print( (' ' * blank_count) + ('*' * start_count) )
