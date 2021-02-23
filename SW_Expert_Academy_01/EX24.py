# 1부터 100 사이의 숫자 중 홀수를 for 문으로 출력
arr =[]
for num in range(1,101) :
    if num % 2 ==1 :
        arr.append(num)

for i in range(len(arr)-1) :
    print(arr[i], end = ', ') # end에 빈 문자열을 지정해서 다음 번 출력이 같은 줄에 오게 됨
print(arr[-1])