#정수를 입력하면 약수를 리스트에 추가해 출력하는 코드를 작성

num = int(input())
factor = []
for k in range(1,num+1) :
    if num % k == 0 :
        factor.append(k)
print(factor)