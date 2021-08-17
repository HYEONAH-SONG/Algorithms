from string import ascii_uppercase
def solution(name_list):
    answer = []
    alpha_list = list(ascii_uppercase)
    # 나를 기준으로 왼쪽에 같은 원소의 갯수를 구한다 --> 갯수 == 인덱스
    for index, value in enumerate(name_list):
        count = name_list[:index].count(value)
        answer.append(str(value+alpha_list[count]))
    return answer

name_list = ["김비바", "김비바", "이비바", "김토스", "이비바", "김비바"]
print(solution(name_list))