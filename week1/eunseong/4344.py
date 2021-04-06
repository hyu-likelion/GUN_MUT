# 평균은 넘겠지

c = int(input())

for i in range (c):
    student = list(map(int, input().split()))
    average = sum(student[1:]) / student[0]
    cnt = 0

    for j in student[1:]:
        if j > average:
            cnt +=1

    percent = cnt/student[0]

    print("{:.3f}%".format(percent*100))
