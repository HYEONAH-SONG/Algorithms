# 표에 적힌 수가 10억보다 적거나 같은 정수 이다.
# N*N  ---> 시간복잡도 o(N)으로 풀면 된다.

import sys
import heapq
# --------------------initialize ---------------
sys.stdin = open("input.txt")
N = int(input())
max_list = []

# --------------------algorithms-------------------
max_num = 0
for n in map(int, input().split()):
    heapq.heappush(max_list,n) # n을 max_list에 맨 마지막 원소로 추가
# print(max_list)
for _ in range(N-1): # 총 N 번
    for n in map(int, input().split()):
        heapq.heappushpop(max_list, n)
        #heap에 n을 푸시한 다음, heap에서 가장 작은 항목을 pop 한다.
print(heapq.heappop(max_list))

# import sys
# import heapq
# # --------------------initialize ---------------
# sys.stdin = open("input.txt")
# N = int(input())
# matrix = [list(map(int,input().split())) for _ in range(N)]
# max_list = matrix[4]
#
# # --------------------algorithms-------------------
# max_num = 0
# reverse_sign = lambda x:x*-1
# for l in reversed(matrix[0:N-1]) :
#     max_list = max_list + l
# stack = []
# for i in range(N):
#     max_list = list(map(reverse_sign, max_list))
#     heapq.heapify(max_list)
#     stack.append(-1 * heapq.heappop(max_list))
#     max_list = list(map(reverse_sign, max_list))
#     heapq.heapify(max_list)
# print(stack.pop())