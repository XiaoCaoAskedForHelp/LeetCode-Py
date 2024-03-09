#    只能被 1 和本身整除的数称为质数。
# 　　请问在 1 （含）到 1000000 （含）中，有多少个质数的各个数位上的数字之和为 23 。
# 　　提示：599 就是这样一个质数，各个数位上的数字之和为 5+9+9=23 。

nums = [True for _ in range(1000001)]
for i in range(2, 1000001):
    if nums[i]:
        index = 2
        tmp = i * index
        while tmp < len(nums):
            nums[tmp] = False
            index += 1
            tmp = i * index
zhi = [i for i in range(len(nums)) if nums[i]]
cnt = 0
for num in zhi:
    sum = 0
    while num:
        sum += (num % 10)
        num = num // 10
    if sum == 23:
        cnt += 1
print(cnt)