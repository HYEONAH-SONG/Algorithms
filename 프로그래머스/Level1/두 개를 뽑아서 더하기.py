# 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더래서 만들 수 있는 모든 수 구하기

def solution(numbers):
    answer = []
    n = len(numbers)
    # start를 차례대로 증가시키며 반복
    for start in range(n):
        for next in range(start+1, n):
            if numbers[start] + numbers[next] in answer:
                continue
            else: answer.append(numbers[start] + numbers[next])
    return sorted(answer)

numbers = [2,1,3,4,1]
print(solution(numbers))