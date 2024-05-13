# 对于一个序列 a[1], a[2], …, a[n]，如果 a[i] 满足 a[i]<a[i-1] 且 a[i]<a[i+1]，则称 a[i] 是一个极小值，如果如果 a[i] 满足 a[i]>a[i-1] 且 a[i]>a[i+1]，则称 a[i] 是一个极大值。
# 　　给定一个序列，请找到极小值中最大的和极大值中最小的。

n = int(input())
nums = [int(i) for i in input().split(' ')]

mins = []
maxs = []
for i in range(1, len(nums) - 1):
    if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
        maxs.append(nums[i])
    elif nums[i] < nums[i - 1] and nums[i] < nums[i + 1]:
        mins.append(nums[i])
print(max(mins), min(maxs))
