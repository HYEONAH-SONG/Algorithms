import sys
import heapq
# --------------------initialize ---------------
sys.stdin = open("input.txt")
N = int(input())
#matrix = [list(map(int,input().split())) for _ in range(N)]
max_list = []

# --------------------algorithms-------------------
max_num = 0
for n in map(int, input().split()):
    heapq.heappush(max_list,n)
for _ in range(1,N):
    for n in map(int, input().split()):
        heapq.heappush(max_list, n)
        heapq.heappop(max_list)
print(he)



reverse_sign = lambda x:x*-1
for l in reversed(matrix[0:N-1]) :
    max_list = max_list + l
stack = []
for i in range(N):
    max_list = list(map(reverse_sign, max_list))
    heapq.heapify(max_list)
    stack.append(-1 * heapq.heappop(max_list))
    max_list = list(map(reverse_sign, max_list))
    heapq.heapify(max_list)
print(stack.pop())