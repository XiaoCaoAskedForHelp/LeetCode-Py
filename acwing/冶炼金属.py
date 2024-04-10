from math import inf

n = int(input())
v_min = 0
v_max = inf
for i in range(n):
    a, b = map(int, input().split())
    v_max = min(v_max, a // b)
    v_min = max(v_min, a // (b + 1) + 1)
print(v_min, v_max)
