n = int(input())

f1 = 1
f2 = 1
f3 = 0

if n >= 20:
    print("0.61803399")
else:
    for _ in range(n - 1):
        f3 = f1 + f2
        f1 = f2
        f2 = f3

    res = f1 / f2
    print('{:.8f}'.format(res))
