# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라

nums = [2,7,11,15]
target = 9

def twoSum (nums,target) :
    sumList = []
    for i in range(len(nums)) :
        for j in range(len(nums)):
            if nums[i] + nums[j] == target and i < j:
                sumList.append(i)
                sumList.append(j)
                print(sumList)
        else :
            continue

twoSum(nums,target)