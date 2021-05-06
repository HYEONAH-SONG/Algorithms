def solution(gems):
    start,end =0,0
    answer=[1,len(gems)]
    dic1 = { gems[0]: 1 }

    for start in range(len(gems)):
        while end < len(gems) and len(dic1) != len(set(gems)):
            if end == len(gems)-1:
                break
            end += 1
            if gems[end] in dic1:
                dic1[gems[end]] += 1
            else:
                dic1[gems[end]] = 1
        if end - start < answer[1] - answer[0]:
            answer = (start + 1, end + 1)
        #     answer[1] = end
        #     answer[0] = start + 1
        if dic1[gems[start]] == 1:
            del dic1[gems[start]]
        else:
            dic1[gems[start]] -= 1
    return answer






gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))