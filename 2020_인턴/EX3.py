def solution(gems):
    start,end =0,0
    answer=[1,len(gems)]
    dic1 = { gems[0]: 1 }

    while start<=end and end<len(gems):
        if len(dic1) != len(set(gems)): # 아직 1이 아닌 요소가 존재함
            end+=1
            if end >= len(gems):
                break
            if gems[end] in dic1:
                dic1[gems[end]] += 1
            else:
                dic1[gems[end]] = 1
        else: # start의 구간을 좁혀야 한다.
            if end - start < answer[1]-answer[0]:
                answer[1]=end+1
                answer[0]=start+1
            if dic1[gems[start]]==1:
                print(gems[start])
                del dic1[gems[start]]
            else:
                dic1[gems[start]]-=1
            start+=1
    return answer



gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))