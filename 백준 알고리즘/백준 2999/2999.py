import sys
sys.stdin = open("input.txt")

alpha = input()
cnt =0

# 입력받은 문자열의 길이를 사용해서 행렬의 가로 세로 크기를 측정하기
for i in range(int(len(alpha)**0.5),0,-1):
    if len(alpha) % i == 0 :
        row = i
        col = len(alpha)// i
        break
# 2차원 리스트 0 초기화
arr = [[0 for _ in range(col)] for _ in range(row)]

# 2차원 리스트에 문자열을 각 칸 마다 대입하기
for i in range(col) :
    for j in range(row) :
        arr[j][i] = alpha[cnt]
        cnt +=1

# 행렬의 문자들을 합쳐서 문자열을 만든다
answer = ''
for brr in arr:
   answer+= ''.join(brr)
print(answer)