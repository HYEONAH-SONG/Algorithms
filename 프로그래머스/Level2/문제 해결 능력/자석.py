import sys
from collections import deque
sys.stdin = open("sample_input.txt")

def calculate(magnet,l,K):
    answer = 0
    # 회전하는 과정
    for i in range(K):
        num, direction = l[i]
        move = [(num-1, direction)]

        # 해당 톱니의 왼쪽 톱니 확인
        d = direction
        for i in range(num -2, -1,-1):
            if magnet[i][2] != magnet[i+1][6]:
                d *= -1
                move.append((i,d))
            else:
                break
        # 해당 톱니의 오른쪽 톱니 확인
        d = direction
        for i in range(num ,4):
            if magnet[i][6] != magnet[i-1][2]:
                d *= -1
                move.append((i,d))
            else:
                break
        # 회전하기
        for num, direction in move:
            if direction == 1: # 시계 방향
                magnet[num].appendleft(magnet[num].pop())
            else: # 시계 반대 방향
                magnet[num].append(magnet[num].popleft())

    # 점수를 매기는 과정
    for i in range(4):
        if magnet[i][0] != 0:
            answer += 2**(i)
    return answer


case = int(input())
for i in range(case):
    K = int(input()) # 회전 횟수
    magnet = []
    l = []
    for index in range(4):
       magnet.append(deque(map(int,input().split())))

    for _ in range(K):
        l.append(list(map(int,input().split())))

    result = calculate(magnet,l,K)
    print("#{} {}".format(i+1,result))