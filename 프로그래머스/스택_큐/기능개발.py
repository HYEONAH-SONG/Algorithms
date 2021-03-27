# 100센트의 진도일때 서비스에 반영 가능
def solution(progresses, speeds):
    answer = []
    l_list=list(zip(progresses,speeds))
    for value in l_list:
        if  (100-value[0])%value[1]==0:
            answer.append( (100-value[0])//value[1])
        else:
            answer.append((100 - value[0]) // value[1]+1)
    return answer

print(solution([93, 30, 55],[1, 30, 5]))