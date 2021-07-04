# 실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
# 시간 복잡도 = 200,000 --> Nlogn
# 최대한 계산량을 줄이는 방법을 생각하자

def solution(N, stages):
    stage_dict = {}
    people = len(stages) # 총 사람의 수
    for i in range(1,N+1): # 1 ~ N
        if people != 0 :
            c = stages.count(i)
            stage_dict[i] = c/people
            people -= c
        else:
            stage_dict[i] = 0
    answer = sorted(stage_dict,key=lambda x:stage_dict[x],reverse=True)
    return answer
N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))