# 1부터 100 사이의 숫자 중 짝수를 for 문을 이용해서 출력하기

arr =[]
for num in range(1,101) :
    if num % 2 ==0 :
        arr.append(num)

for i in range(len(arr)) :
    print(arr[i], end = ' ') # end에 빈 문자열을 지정해서 다음 번 출력이 같은 줄에 오게 됨