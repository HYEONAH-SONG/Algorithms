import sys
sys.stdin = open("input.txt")

case = int(input())
for _ in range(case):
    num = int(input())
    matrix = [list(map(int,input().split())) for _ in range(num)]


for i in range(case):
    sum = 0
    for j in range(case):

