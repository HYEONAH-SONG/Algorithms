# 배열을 입력받아 합으로 0을 만들 수 있는 3개의 원소를 출력하라

nums = [-1,0,1,2,-1,-4]
nums = sorted(nums)  # -4,-1,-1,0, 1,2

# 브루트 포스로 계산
def threeSum(nums):
    zero = []

    for i in range(len(nums)):
        # 중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1,len(nums)):
            # 중복된 값 건너뛰기
            if j > 0 and nums[i] == nums[i-1]:
                continue
            for k in range(j + 1, len(nums)):
                sum = []
                if nums[i] + nums[j]+ nums[k] == 0:
                    sum.append(nums[i])
                    sum.append(nums[k])
                    sum.append(nums[j])
                    zero.append(sorted(sum))
    return zero

def threeSum2(nums):
    zero = []

    for i in range(len(nums)-2):
        # 중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums)-1):
            # 중복된 값 건너뛰기
            if j > i+1 and nums[j] == nums[j - 1]:
                continue
            for k in range(j + 1, len(nums)):
                if k > i+1 and nums[k] == nums[k - 1]:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    zero.append((nums[i],nums[j],nums[k])) # append 내부에 여러 값이 들어가면 자체적으로 리스트를 형성
    return zero

# 투 포인터로 합 계산
def threeSum3(nums):

    zero = []
    for i in range(len(nums)-2):
        # 중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i+1, len(nums)-1
        while left < right:
            sum = nums[i]+nums[left]+nums[right]
            if sum < 0 :
                left +=1
            elif sum > 0:
                right -=1
            else:
                zero.append((nums[i],nums[left],nums[right]))
                while left <right and nums[left] == nums[left+1]:
                    left+=1
                while left < right and nums[right] == nums[right-1]:
                    right -=1
                left +=1
                right -=1

    return zero

print(threeSum(nums))
print(threeSum2(nums))
print(threeSum3(nums))