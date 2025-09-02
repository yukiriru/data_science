# for num in range(1,101) :
#     print(num)
#
# print("*"*20)

# num = 1
# sum = 0
# while num <= 1000:
#     if num % 3 == 0:
#         sum+=num
#     num+=1
# print(sum)

score = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0
for num in range(len(score)):
    sum +=score[num]
print(sum/len(score))

STAR =5
for num in range(1,1+STAR):
    print("*"*num)

STAR =5
for num in range(1,1+STAR):
    print(" "*(STAR-num) + "*"*num)

star = int(input("삼각형의 높이를 입력하세요: "))
for num in range(1,1+star):
    print(" "*(star-num) + "*"*num)