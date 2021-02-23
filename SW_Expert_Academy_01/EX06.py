# 1~200 사이의 정수 가운데 7의 배수이면서 5의 배수는 아닌 숫자

arr =[]
for i in range (1,201) :
   if i%7 ==0 and  i%5 != 0 :
       arr.append(i)

for i in range(len(arr)-1) :
    print(arr[i],end=',')
print(arr[-1])