s = input()
cnt = 0
i = 0
while i < len(s) - 1:
    if s[i] == s[i + 1] or s[i] == '?' or s[i + 1] == '?':
        cnt += 1
        i += 2
    else:
        i += 1

print(cnt)
