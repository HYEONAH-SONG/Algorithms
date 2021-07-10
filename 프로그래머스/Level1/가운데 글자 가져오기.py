# 단어의 길이가 홀수인 경우 --> 가운데 한 글자
# 단어의 길이가 짝수인 경우 --> 가운대 두 글자
def solution(s):
    if len(s)%2 == 0 : # 짝수인 경우
        return s[len(s)//2-1:len(s)//2+1]
    else : # 홀수인 경우
        return s[len(s)//2]
s = "abcdeeee"
print(solution(s))