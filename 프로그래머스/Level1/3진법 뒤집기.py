# n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현
# 3진법을 표현하는 방법
def ternary_make(num):
    ternary = ''
    while num > 0:
        num, mod = divmod(num,3)
        ternary += str(mod)
    return ternary

def solution(n):
    ternary = ternary_make(n)
    answer = int(ternary,3)
    return answer

print(solution(45))