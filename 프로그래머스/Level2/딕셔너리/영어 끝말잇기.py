# 시간 복잡도 : O(n) --> n = 100
def solution(n, words):
    check = {}
    stack = []
    division = [i if i != 0 else n for i in range(n)] # 나머지

    for count,word in enumerate(words):
        if word in check : # 이전에 등장했던 단어인 경우
            return [division[(count+1)%n], count//n+1]
        elif stack and word[0] != stack.pop(): # 이전 단어의 끝과 현재 단어의 앞이 다른 경우
            return [division[(count+1)%n], count//n+1]
        else: # 그 외 진행이 잘 되는 경우
            stack.append(word[-1])
            check[word] = 1
    return [0,0]
n, words = 2, 	["hello", "one", "even", "never", "now", "world", "draw"]
print(solution(n, words))