def solution(s):
    count = 0
    s = s.lower()
    for i in s:
        if i == "p": # p인 경우
            count +=1
        elif i =="y": # y인 경우
            count -=1
        else: continue # 그 외의 알파벳인 경우
    if count != 0 :
        return False
    return True

def solution2(s): # another solution
    return s.lower().count('p') == s.lower().count('y')

s = "pPoooyY"
print(solution(s))