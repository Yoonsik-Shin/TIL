def maxSubArray(nums):
    total_max = nums[0]
    cur_max = nums[0]

    for i in range(1, len(nums)):
        cur_max = max(nums[i] + cur_max, nums[i])
        total_max = max(total_max, cur_max)

    return total_max

n = int(input())
numbers = list(map(int,input().split()))
print(maxSubArray(numbers))