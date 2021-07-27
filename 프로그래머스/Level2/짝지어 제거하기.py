def solution(s):
    stack = []
    for word in s:
        if len(stack) == 0: # 스택이 비어있는 경우
            stack.append(word)
        elif stack[-1] == word: # 연속적으로 같은 알파벳이 존재하는 경우
            stack.pop()
        else:
            stack.append(word)
    if len(stack) == 0:
        return 1
    return 0