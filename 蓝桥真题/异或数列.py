t = int(input())
# 异或 1 & 0 = 1     0 & 0 = 1 碰到0 是不变的，所以能改变的只有1
# A和B（二进制）从高到低有一位不同时，是1的那个人赢
# 计算最高位1的个数
# 偶数个1,ab相等比较下一位
# 奇数个1的时候，需要拿到最后一个1才能赢
# 奇数个1并且0是偶数个的时候，先手拿一个1，之后后手选啥，先手就选什么（让B陷入双偶局面），先手赢
# 奇数个1并且0是奇数个的时候，先手不管拿什么，后手就跟你拿相反的，后手赢（除非只有一个1）
for _ in range(t):
    nums = [int(i) for i in input().split()]
    res = 0
    for i in range(20, -1, -1):
        cnt = 0
        for j in range(1, len(nums)):
            cnt += (nums[j] >> i) & 1
        if cnt % 2 == 0:
            continue
        else:
            if cnt == 1:
                res = 1
            elif nums[0] % 2 == 1:
                res = 1
            else:
                res = -1
            break
    print(str(res))
