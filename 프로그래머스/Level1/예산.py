# 최대한 많은 부서의 물품을 구매해 줘야함
# 총 합이 budget이 되는 최대의 경우의 수를 구해야 함 --> 최소의 값부터 살펴보자
# 예산을 안넘는 한에서 최소의 값부터 count해야한다.
def solution(d, budget):
    new = sorted(d)
    answer = 0
    for i in range(len(new)):
        if new[i] <= budget:
            answer +=1
            budget -= new[i]
        else:break
    return answer

d = [1,3,2,5,4]
budget = 9
print(solution(d,budget))