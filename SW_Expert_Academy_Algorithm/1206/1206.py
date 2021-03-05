#1206
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


# 이중 for문과 min()을 이용하기 때문에 시간 복잡도 : O(n^2) + O(n) = n^2
# 10 * 1000
# 10번의 테스트 케이스를 반복하면서 각 테스트 케이스마다 가지는 길이를 인덱스로 사용해서 조망권이 확보된 세대의 수를 찾았다
# 왼쪽 오른쪽 2 칸 이내에 있는 건물은 반드시 자신의 건물 최대 높이 보다 낮아야 한다
