
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

matrix = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']] # 키패드
keypad = {1: (0, 0), 2: (0, 1), 3: (0, 2),
          4: (1, 0), 5: (1, 1), 6: (1, 2),
          7: (2, 0), 8: (2, 1), 9: (2, 2),
          '*': (3, 0), 0: (3, 1), '#': (3, 2)}
def cal(keypad,left,right,v):
    dist_left =  abs(keypad[left][0] - keypad[v][0]) + abs(keypad[left][1] - keypad[v][1])
    dist_right = abs(keypad[right][0] - keypad[v][0]) + abs(keypad[right][1] - keypad[v][1])
    distance=[dist_right,dist_left]
    return distance

def solution(numbers, hand):
    answer = ''
    left = '*'
    right ='#'

    for i,v in enumerate(numbers):
        if v == 1 or v ==4 or v== 7 :
            answer+='L'
            left = v

        elif v == 3 or v == 6 or v == 9:
            answer += 'R'
            right = v

        else : # 2,5,8,0
            # 거리 계산
            distance = cal(keypad,left,right,v)
            if (distance[0]>distance[1]) or (distance[1]==distance[0] and hand =="left") :
                answer+='L'
                left = v
            elif (distance[1]>distance[0]) or (distance[1]==distance[0] and hand =="right"):
                answer +='R'
                right =v
    return answer

#
# numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
# hand = "right"
# result = solution(numbers,hand)
# print(result)
# 1. 1,4,7 : 무조건 왼손
# 2. 3,6,9 : 무조건 오른손
# 3. 2,5,8,0은 더 가까운 거리의 손
# 4. 만약 같은 거리가 나오는 경우에는 HANDS에 따라 결정됨
# 거리 계산은 BFS
# n^3 나오면 안됨
