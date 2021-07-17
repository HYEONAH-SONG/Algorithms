#다음 100X100의 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램을 작성하여라.
#1209
import sys
sys.stdin = open("input.txt")

for _ in range(10):
    num = int(input()) # 2021 카카오페이 인턴 case number
    total = [] # 대각선, 가로, 세로의 합을 저장하는 리스트
    array = [] # 전체 행렬을 저장하는 리스트

    for j in range(100): # 행
        row = list(map(int, input().split())) # 각 row에 들어가는 list
        array.append(row) # 각 row를 추가하기

# 헹렬만들기 완료
    diagonal_sum, diagonal2_sum = 0, 0
    for j in range(100): # 행
        row_sum, col_sum = 0, 0  # init
        for i in range(100): # 열
            row_sum += array[j][i]
            col_sum += array[i][j]
            if j == i:
                diagonal_sum += array[j][i]
            elif j == 99 - i:
                 diagonal2_sum += array[j][i]

        if not total or total[-1]<= row_sum:
            total.append(row_sum)
        if not total or total[-1] <= col_sum:
            total.append(col_sum)
    # print(num, total)
    if not total or total[-1] <= diagonal_sum:
        total.append(diagonal_sum)
    if not total or total[-1] <= diagonal2_sum:
        total.append(diagonal2_sum)

    print("#{} {}".format(num,total[-1]))
