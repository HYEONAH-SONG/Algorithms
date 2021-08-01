# 문제 : 1개 이상의 단위로 문자열을 잘라 압축하여 표현한 문자열중 가장 짧은 것의 길이를 return
# 문제 해결 방법 : pattern을 찾자 --> pattern 내에 문자가 많을 수록 짧아진다.(연속해서 있는 것이 포인트)

def solution(s):
    answer = 0
    element = len(s)
    print(s.count("a"))
    return answer
s = "aabbaccc"
print(solution(s))