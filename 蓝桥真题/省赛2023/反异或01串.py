# 超时、内存溢出
# t = input()
#
# # 关键：求1数量最多的回文子串，因为可以使用反异或的操作节省一半的1
# num = t.count("1")
# n = len(t)
# dp = [[-1] * n for _ in range(n)]
# for i in range(n):
#     if t[i] == "1":
#         dp[i][i] = 1
#     else:
#         dp[i][i] = 0
# max1 = 1
# for i in range(n - 1, -1, -1):
#     for j in range(i + 1, n):
#         if j - i == 1:
#             if t[i] == t[j]:
#                 dp[i][j] = (2 if t[i] == "1" else 0)
#         else:
#             # 中间那一位不能为1
#             if dp[i + 1][j - 1] != -1 and \
#                     ((j - i + 1) % 2 == 0 or ((j - i + 1) % 2 == 1 and t[(i + j) // 2] != "1")) \
#                     and t[i] == t[j]:
#                 dp[i][j] = dp[i + 1][j - 1] + (2 if t[i] == "1" else 0)
#         max1 = max(max1, dp[i][j])
# print(num - max1 // 2)


def manacher(s):
    s = "#" + "#".join(s) + "#"
    n = len(s)
    right = -1
    c = -1
    l = 0
    arm_len = []
    ones = 0
    pre = [0] * (n + 1)  # 1的前缀和，用来方便计算1的
    for i in range(1, n):
        pre[i] = pre[i - 1] + (s[i] == "1")
    for i in range(n):
        if right > i:
            i_sym = 2 * c - i
            l = min(arm_len[i_sym], right - i)
        else:
            l = 1
        while i + l < n and i - l >= 0 and s[i + l] == s[i - l]:
            l += 1
        arm_len.append(l)
        if i + l > right:
            right = i + l
            c = i
        if s[i] != "1":  # 中心点不能为1
            ones = max(ones, pre[i + l - 1] - pre[i - l + 1])
    return ones


s = input()
num = s.count("1")
sub = int(manacher(s) // 2)
print(num - sub)
