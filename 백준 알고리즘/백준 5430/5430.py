# 명령어의 최대 길이 : 100,000
# 최대  테스트 케이스 갯수 : 100
# 명령어의 길이 합과 배열에 들어있는 수의 합  최대 : 700,000
from collections import deque
import sys
sys.stdin = open("input.txt")

def AC(command,len,arr):

    for i in command:
        if i == "R":
            print("hi")
        if i == "D" and arr: # D 명령어 + arr 값 존재
            arr.pop()
        else :
            return print("error")
    return arr


case = int(input())
for i in range(case):
    arr = deque()
    command = list(input())
    len = int(input())
    arr = input()[1:-1].split(',')
    print("CASE:",i+1)
    print(arr)
    print(AC(command,len,arr))




