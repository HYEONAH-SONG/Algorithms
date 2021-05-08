def solution(s):
    answer = []
    alpha = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8,
             "nine": 9}
    stack =""

    for i in s:
        stack+=i
        for key in alpha:
            if stack.find(key)>=0:
                answer.append(str(alpha[key]))
                stack=""
            elif str(alpha[key]) in stack:
                answer.append(str(alpha[key]))
                stack=""
            else: continue
    answer_ = int("".join(answer))
    return answer_

s =  "1zerotwozero3"
print(solution(s))