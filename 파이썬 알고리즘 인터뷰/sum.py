# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라
# enumerate를 활용하여 부르트 포스 알고리즘
nums = [2,7,11,15]
target = 9
sum =[]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if target == nums[j] + nums[i]:
            sum.append(i)
            sum.append(j)
print(sum)


dict={}
for index,value in enumerate(nums):
    dict[value] = index
print(dict)

for nums,index in dict.items():
    if target - nums in dict:
        l=[index,dict[target-nums]]
print(l.so)