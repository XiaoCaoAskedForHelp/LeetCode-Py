k = int(input())
s = input()
if len(s) % k != 0:
    print(-1)
else:
    l = len(s) // k
    total = [[0] * 26 for _ in range(l)]  # 记录每一个循环中对应位置上各字母的统计
    for j in range(l):  # 遍历循环中的字母
        for i in range(0, k):  # 遍历每一个循环
            total[j][ord(s[i * l + j]) - ord('a')] += 1
    maxs = [max(nums) for nums in total]
    sums = [sum(nums) for nums in total]
    print(sum([i - j for i, j in zip(sums, maxs)]))
