# 100~300 사이의 숫자에서 각각의 자리 숫자가 짝수인 숫자를 찾아서 콤마(,)로 구분

arr =[]

for i in range (100,301) :
   if (i //100)%2 ==0 and ((i%100)//10)%2 ==0 and (i%10)%2==0:
       arr.append(i)

for i in range(len(arr)-1) :
    print(arr[i],end=',')
print(arr[-1])