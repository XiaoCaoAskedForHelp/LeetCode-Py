from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
a.sort()
dic = defaultdict(int)
for i in a:
    dic[i] += 1
m = a[0]
while True:
    if dic[m] % (m + 1) == 0:
        dic[m + 1] += dic[m] // (m + 1)
        m += 1
    else:
        break
print(m)
