import sys
sys.stdin = open("input.txt")

word = (input()).upper()  # 입력받은 단어를 대문자로 변환

dict1 = dict() # 가장 많이 사용된 알파벳 알아내기 위한 딕셔너리 정의

for i in word :
   if i in dict1 :
        dict1[i] +=1
   else:
        dict1[i] =1

m = max(dict1.values()) #딕셔너리 값 중에서 최대값을 정의
cnt =0 # 최댓값이 나오는 횟수
for key, value in dict1.items():
    if value == m :
        cnt += 1
        j = key
if cnt > 1: # 최대값의 횟수가 1보다 큰 경우 ? 출력
    print("?")
else :
    print(j)

# 1157
# (0,0) -> queue에 출발점 넣음
# queue 에 하나씩 꺼내서 4방향 보고
# 하나씩 본것을 갈 수 있는지 없는지 판별
# (0,0) -> queue에 출발점 넣음
# queue 에 하나씩 꺼내서 4방향 보고
# 하나씩 본것을 갈 수 있는지 없는지 판별
# (0,0) -> queue에 출발점 넣음
# queue 에 하나씩 꺼내서 4방향 보고
# 하나씩 본것을 갈 수 있는지 없는지 판별
# (0,0) -> queue에 출발점 넣음
# queue 에 하나씩 꺼내서 4방향 보고
# 하나씩 본것을 갈 수 있는지 없는지 판별
# 하나씩 본것을 갈 수 있는지 없는지 판별
# (0,0) -> queue에 출발점 넣음
# queue 에 하나씩 꺼내서 4방향 보고
# 하나씩 본것을 갈 수 있는지 없는지 판별
# (0,0) -> queue에 출발점 넣음
# queue 에 하나씩 꺼내서 4방향 보고
# 하나씩 본것을 갈 수 있는지 없는지 판별
# (0,0) -> queue에 출발점 넣음
# queue 에 하나씩 꺼내서 4방향 보고
# 하나씩 본것을 갈 수 있는지 없는지 판별
