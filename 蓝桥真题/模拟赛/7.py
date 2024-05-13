# 给定一个仅包含数字字符的字符串，请统计一下这个字符串中出现了多少个值为奇数的数位。

s = input()
cnt = 0
for i in s:
    if int(i) % 2:
        cnt += 1
print(cnt)
