import sys
sys.stdin = open("input.txt")

for j in range(10) : #테스트케이스 10번
    cnt = 0 # 조망권 건물 갯수
    length = int(input()) #전체 전물의 갯수
    arr = list(map(int, input().split())) # 각 건물의 최대 층수
    for i in range(2,length-2): # 왼쪽 오른쪽 2칸 이내에서 해당 건물의 최대 층수가 가장 큰 경우에는 cnt를 더해준다
        if arr[i]-arr[i+1] >0 and arr[i]-arr[i-1]>0 and arr[i]-arr[i+2] >0 and arr[i]-arr[i-2]>0:
             cnt += min(arr[i]-arr[i+1],arr[i]-arr[i-1],arr[i]-arr[i+2],arr[i]-arr[i-2])

    print("#{} {}".format(j+1,cnt))