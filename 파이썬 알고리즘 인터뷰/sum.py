# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라
# enumerate를 활용하여 부르트 포스 알고리즘
nums = [2,7,11,15]
target = 9

def twoSum (nums,target) :
    sumList = []
    for i in range(len(nums)) :
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target :
                sumList.append(i)
                sumList.append(j)
                return sumList
        else :
            continue

def twoSum2(nums,target):
    nums_map={}
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target-num],i]
        nums_map[num] = i

print(twoSum(nums,target))
print(twoSum2(nums, target))