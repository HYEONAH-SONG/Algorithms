# 1부터 45까지의 숫자 중 6개를 찍어서 맞히는 복권

def solution(lottos, win_nums):
    answer = []
    rank = [6,6,5,4,3,2,1]
    # 0,1,2,3,4,5,6 --> 인덱스 = 맞춘 수 / 값 = 순위
    count = 0
    zero = lottos.count(0) # 낙서로 보이지 않은 원소의 갯수
    for i in lottos:
        # 0을 제외하고 당점 번호에 포함된 원소들을 카운트
        if i in win_nums:
            count +=1
    answer.append(rank[count + zero]) # 최고 순위
    answer.append(rank[count]) # 최저 순위
    return answer

lottos,win_nums = [44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums))