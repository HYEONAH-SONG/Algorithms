def solution(gems):
    start,end = 0,0
    gems_dict = dict()

    while end < len(gems): # 모든 원소에 VALUE가 1 이상이 되는 경우까지 ---> 충족하는 경우에는 앞에서 부터 빼면서 다 1이 되는 지를 확인하기
        if gems[end] in gems_dict:
            gems_dict[gems[end]] +=1
        else: gems_dict[gems[end]] = 1
        end += 1 # end는 잘 나옴
    # print(gems_dict)
        if len(set(gems)) == len(gems_dict):
            while start<end: # 모두다 1 이상인 경우 --> start를 앞당겨 보기
                if gems_dict[gems[start]]>1:
                    gems_dict[gems[start]] -= 1
                    start+= 1
                # print(gems_dict)
                elif len(gems)> end -start:
                    short = end -start
                    answer = [start+1,end]
                    break
                else:
                    break
    return answer



gems = ["AA", "AB", "AC", "AA", "AC"]
print(solution(gems))