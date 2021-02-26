import sys
sys.stdin = open("input.txt")

T = int(input()) #테스트 케이스의 개수
isTrue = False
for _ in range(T) :
    str = input()
    for i in range(len(str)-1):
        if str.count("(") == str.count(")") and str[-1] ==")" and str[0] =="(" and str[:i].count("(") >= str[:i].count(")"):
            isTrue = True #시작과 끝은 (), 절대로 이전의 문자열에서 )의 갯수가 더 많아서는 안된다
        else:
            isTrue = False
            break
    if isTrue == True:
        print("YES")
    else :
        print("NO")