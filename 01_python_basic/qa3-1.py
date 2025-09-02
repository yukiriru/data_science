while(True) :
    num = int(input("대각선 가로축의 길이를 홀수로 입력하세요(-1 종료): "))
    if num == -1 :
        exit()
    elif num % 2 == 0 :
        print("가로축의 길이는 홀수여야 합니다.")
    else :
        for n in range(num):
            if num // 2 > n :
                print("|" + " " * (num //2 -n) + "*" * (2*n+1) + " " * (num //2 -n)+"|")
            elif num // 2 == n :
                print("|"+ "*" * num + "|")
            else :
                print("|" + " " * (n -num // 2) + "*" * ((num-n)*2 -1) + " " * (n - num // 2)+ "|")
