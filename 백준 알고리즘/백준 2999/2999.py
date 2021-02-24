import sys
sys.stdin = open("input.txt")

alpha = input()
num = len(alpha)
list1 =[]

for i in range(int(num**0.5),0,-1):
    if num % i == 0 :
        row = i
        col = num // i
        break
arr = [[0 for _ in range(col)] for _ in range(row)]

cnt =0


for i in range(col) :
    for j in range(row) :
        arr[j][i] = alpha[cnt]
        cnt +=1


answer = ''
for brr in arr:
   answer+= ''.join(brr)
print(answer)