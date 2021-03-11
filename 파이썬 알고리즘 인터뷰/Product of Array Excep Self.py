# 배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의  곱셈 결과가 되도록 출력하라

arr = [1,2,3,4]


multi_list = []
for i in range(len(arr)):
    left, right = 0, len(arr) - 1
    multi = 1
    while left < right :
        if left < i : # 자신의 왼쪽 요소들 곱하기
            multi *= arr[left]
            left+=1
        elif right > i : # 자신의 오른쪽 요소들 곱하기
            multi *= arr[right]
            right -= 1
        else:
            continue
    multi_list.append(multi)
print(multi_list)