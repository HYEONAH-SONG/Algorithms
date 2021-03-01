import sys
sys.stdin = open("input.txt")

T = int(input()) #테스트 케이스의 개수
isTrue = False
for _ in range(T) :
    str = input()
    for i in range(len(str)-1):
        if str.count("(") == str.count(")") and str[-1] ==")" and str[0] =="(" and str[:i].count("(") >= str[:i].count(")"):
            isTrue = True # 괄호 성립 조건 true
        else:
            isTrue = False
            break
    if isTrue == True:
        print("YES")
    else :
        print("NO")

# 시간복잡도 : 이중 for문을 사용하면서 .count() 함수를 사용하기 때문에 O(n^2) + O(n) = n^2 이 된다.
# 시작과 끝은 ()이고, 절대로 이전의 문자열에서 )의 갯수가 더 많아서는 안된다