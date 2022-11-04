#5597 과제 안 내신 분..?

student = [0] * 30

for _ in range(28):
    sub = int(input())
    student[sub - 1] = 1

for i in range(len(student)):
    if student[i] == 0:
        print(i + 1)