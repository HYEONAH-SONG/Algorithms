#  #인 부분은 1 공백인 부분은 0
#  # 이 하나라도 있으면 무조건 포함
#  공백은 둘다 만족
# 원래의 비밀지도를 해독하기
def bin(num):
    result = ''
    arr = ['0', '1']
    while num > 0:
        result = arr[num % 2] + result
        num = num // 2
    return result

def solution(n, arr1, arr2):
    secret_map = []
    for decimal1, decimal2 in zip(arr1, arr2):
        # 1인 부분이 하나라도 있으면 포함 --> XOR
        element = str(bin(decimal1 | decimal2))
        print(element)
        # n의 자릿수로 만들기
        while len(element)< n :
            element = '0'+ element

        element = element.replace('1', '#')
        element = element.replace('0', ' ')
        secret_map.append(element)
    return secret_map

n,arr1,arr2 =5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]
print(solution(n, arr1, arr2))