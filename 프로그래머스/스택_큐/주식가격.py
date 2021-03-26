# 초 단위로 기록된 주식가격이 담긴 배열이 매개변수로 주어질 때,
# 가격이 떨어지지 않은 기간은 몇 초 인지 return 하도록 solution 함수를 완성하기

def solution(prices):
    stack=[]
    answer = [0]*len(prices)
    for index,cur_price in enumerate(prices):
        while stack and cur_price >= prices[stack[-1]]:
            last = stack.pop()
            answer[index]=index-last
        stack.append(index)
    return answer

prices = [1, 2, 3, 2, 3]
print(solution(prices))