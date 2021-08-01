# 시간 복잡도 : 1,000 * 1,000
# 푸는데 걸리는 시간 : 20분

def solution(citations):
    stack = []
    size = len(citations)+1 # n 편의 논문
    for num in range(0,size):
        up, down = 0, 0
        for i in citations:
            if i >= num: # h 번 이상 인용된 논문 갯수
                up +=1
            else : # 나머지 논문 갯수
                down +=1
        if up >= num and down<=num:
            stack.append(num)
    return stack.pop()

citations = [3, 0, 6, 1, 5]
print(solution(citations))