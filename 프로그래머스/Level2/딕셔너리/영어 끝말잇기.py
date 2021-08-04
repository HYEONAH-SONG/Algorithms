def solution(n, words):
    count = 0
    d = dict()
    stack = []
    division = [i if i != 0 else n for i in range(n+1)]
    for i in words:
        count += 1
        if i in d : # 끝말잇기가 끝나는 조건
            return [division[count%n],count//n]
        elif stack and i[0] != stack.pop():
            return [count % n, count // n]
        else:
            stack.append(i[-1])
            d[i] = 1
    return [0,0]