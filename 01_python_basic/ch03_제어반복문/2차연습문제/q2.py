num = 1
sum = 0

while num <= 1000:
    if num % 3 == 0:
        sum += num
    num += 1

print("3의 배수의 합:", sum)
