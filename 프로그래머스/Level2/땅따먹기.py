# N행 4열 --> 열의 갯수가
# 각 행의 한 칸만 밟으면서 내려와야 한다.
# 같은 열을 "연속"해서 밟을 수 없다.
# def solution(land):
#     answer = 0
#     num,max = 0,0
#     score = [] # 이전 arr의 최댓값의 index를 저장
#     for arr in land:
#         new = sorted(arr)
#         for index,value in enumerate(arr):
#             if new[-1] == value:
#                 num = index # 최댓값의 인덱스
#                 max = value # 최댓값
#         if score:
#             n = score.pop()
#             if n != num:
#                 answer += max
#                 score.append(num)
#             elif n == num:
#                 answer += new[-2]
#                 score.append(arr.index(new[-2]))
#         else: # 처음의 경우
#             score.append(num)
#             answer += max
#     return answer
#

def solution(land):
    for i in range(0,len(land)-1):
        for j in range(4):
            land[i + 1][j] = land[i + 1][j] + max(land[i][0:j] + land[i][j+1:])
    return max(land[-1])

land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land))