# def solution(s):
#     answer = []
#     # 답으로 출력되는 문자열
#
#     alpha = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8,
#              "nine": 9}
#     # 0~9까지 딕셔너리 매핑
#     word = ""
#
#     for i in s:
#         word += i
#         for key in alpha:
#             if word.find(key)>=0: # alphabet 이 존재하는 경우 --> find 함수를 사용하여 key에 대한 인덱스가 반환됨
#                 answer.append(str(alpha[key]))
#                 word = ""
#             elif str(alpha[key]) in word: # 숫자가 존재하는 경우
#                 answer.append(str(alpha[key]))
#                 word = ""
#             else: # 아무것도 존재하지 않는 경우
#                 continue
#     answer_ = int("".join(answer))
#     return answer_
#
#
# s = "1zerotwozero3"
# print(solution(s))


def solution(s):
    answer = []
    # 답으로 출력되는 문자열

    alpha = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8,
             "nine": 9}
    # 0~9까지 딕셔너리 매핑
    word = ""

    for i in s:
        word += i
        for key in alpha:
            if key in word: # alphabet 이 존재하는 경우
                answer.append(str(alpha[key]))
                word = ""
            elif str(alpha[key]) in word: # 숫자가 존재하는 경우
                answer.append(str(alpha[key]))
                word = ""
            else: # 아무것도 존재하지 않는 경우
                continue
    answer_ = int("".join(answer))
    return answer_

s = "1zerotwozero3"
print(solution(s))