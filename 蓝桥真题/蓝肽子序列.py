str1 = input()
str2 = input()

str1s = []
pre = 0
for i in range(1, len(str1)):
    if 'A' <= str1[i] <= 'Z':
        str1s.append(str1[pre:i])
        pre = i
str1s.append(str1[pre:])

pre = 0
str2s = []
for i in range(1, len(str2)):
    if 'A' <= str2[i] <= 'Z':
        str2s.append(str2[pre:i])
        pre = i
str2s.append(str2[pre:])

# str1和str2中i，j长度的子串相同的长度
dp = [[0] * (len(str2s) + 1) for _ in range((len(str1s) + 1))]
for i in range(1, len(str1s) + 1):
    for j in range(1, len(str2s) + 1):
        if str1s[i - 1] == str2s[j - 1]:
            # 如果这两个字符串相等
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp[-1][-1])

