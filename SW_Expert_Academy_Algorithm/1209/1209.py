#다음 100X100의 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램을 작성하여라.
#1209
import sys
sys.stdin = open("input.txt")

for j in range(10):
    num=int(input())
    sum1 = 0
    sum2 = 0
    sum3 =0
    sum4 = 0
    large = [] #2차원 행렬
    maximum = [] # 대각선, 가로, 세로의 각 합에 대한 리스트
    for i in range(100):
        small=input()
        n_small = list(map(int,small.split()))
        large.append(n_small)

    for i in range(100):
        sum1 += large[i][i]
        sum2 += large[i][99-i]
        for j in range(100):
            sum3+=large[0][j]

            sum4+=large[j][0]
        maximum.append(sum3)
        maximum.append(sum4)
    maximum.append(sum1)
    maximum.append(sum2)

    print(maximum)


