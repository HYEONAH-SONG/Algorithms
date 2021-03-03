#다음 100X100의 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램을 작성하여라.

import sys
sys.stdin = open("input.txt")

for _ in range(10):
    num=int(input())
    large = []
    for i in range(100):
        small=input()
        small = list(map(int,small.split()))
