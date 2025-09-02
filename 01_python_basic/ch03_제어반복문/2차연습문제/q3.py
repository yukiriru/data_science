scores = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0

for score in scores:
    total += score

average = total / len(scores)
print("A 학급의 평균 점수:", average)