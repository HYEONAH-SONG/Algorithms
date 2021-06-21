# 주사위를 던져서 나오는 값들의 빈도를 계산하여 출력하는 프로그램을 작성하시오.
#    즉 1, 2, 3, 4, 5, 6의 값이 1000번의 시도 중 각각 몇 번이나 나오는지를 계산한다. 난수 발생 함수와 리스트를 사용하시오. [10]
import random

dice = [0,0,0,0,0,0]
for _ in range(1000):
    d = random.randrange(1,7)
    if d == 1:
        dice[0] += 1
    elif d ==2:
        dice[1] +=1
    elif d ==3:
        dice[2] +=1
    elif d ==4:
        dice[3] +=1
    elif d ==5:
        dice[4] +=1
    else :
        dice[5] +=1
print(dice)