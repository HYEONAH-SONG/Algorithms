from collections import deque

a = deque([1,2,3])
b = list()
a.appendleft(0)
print(a)
a.popleft()
print(a)

# collections 덱큐
