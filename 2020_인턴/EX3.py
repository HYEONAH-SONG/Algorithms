def solution(gems):
    end = 0
    gems_dict = dict()
    global start
    for start in range(len(gems)):
        while len(set(gems)) > len(gems_dict) and end < len(gems): # 모든 원소에 VALUE가 1 이상이 되는 경우까지 ---> 충족하는 경우에는 앞에서 부터 빼면서 다 1이 되는 지를 확인하기
            k = gems[end]
            if k in gems_dict:
                gems_dict[k] +=1
            else: gems_dict[k] = 1
            end += 1

        while len(set(gems)) == len(gems_dict) and 0 not in gems_dict.values(): # 모두다 1 이상인 경우 --> start를 앞당겨 보기
            p = gems[start]
            gems_dict[p] -= 1
        return [start,end]


gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))