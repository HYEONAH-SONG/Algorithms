# 초 단위로 기록된 주식가격이 담긴 배열이 매개변수로 주어질 때,
# 가격이 떨어지지 않은 기간은 몇 초 인지 return 하도록 solution 함수를 완성하기

def solution(prices):
    stack=[]
    answer = [0]*len(prices)
    for index,cur_price in enumerate(prices):
        # 현재의 값이 이전의 값 보다 작은 경우에는 1초가 무조건 answer에 적힌다.
        while stack and cur_price < prices[stack[-1]]:
            last = stack.pop()
            answer[last]=index-last
        stack.append(index) # 0,1,3,4
    # 0,0,1,0,0 ---> 세번째만 자신 보다 가격이 떨어지는 날 존재
    while stack:
        second = stack.pop()
        answer[second] = len(prices) - (second+1)
    return answer

prices = [1, 2, 3, 2, 3]
print(solution(prices))