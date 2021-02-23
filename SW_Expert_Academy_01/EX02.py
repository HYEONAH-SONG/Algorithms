import sys

num = int(input())
cnt = 0
arr =[]

for k in range(1, num+1):
    if num % k == 0 :
        print(str(k) + "(은)는 "+ str(num) + "의 약수입니다.")
        cnt = cnt +1
        arr.append(k)
if cnt ==2:
    print(str(num)+ "(은)는 " + str(arr.pop(0))+ " 와 " + str(arr.pop(0)) + "로만 나눌 수 있는 소수입니다")