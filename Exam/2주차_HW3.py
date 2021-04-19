import random

count = int(input('주사위 실험 횟수를 입력하시오: '))
count_num = count
total = [0 for _ in range(36)]

while count > 0:
    x_1 = random.randint(1,6) # 1 <= x_1 <= 6
    x_2 = random.randint(1, 6)  # 1 <= x_2 <= 6
    sum = x_1 + x_2
    total[sum]+=1
    count-=1

for i in range(2,13):
    rate = (total[i] / count_num)*100
    print(i,round(rate,3),"%")