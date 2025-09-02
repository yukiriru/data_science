# range(시작인덱스, 마지막인덱스+1)
a = range(1,11)
print(f"a: {a}")

for index in a:
    print(index)

b = range(10) # 인자가 1개인 경우는 0~인자값-1까지의 범위
print(f"b: {b}")
for index in b:
    print(index)

total = 0
for number in range(1,11):
    total += number

print(f"total: {total}")