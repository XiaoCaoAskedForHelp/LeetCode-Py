# 请问 2023 有多少个约数？即有多少个正整数，使得 2023 是这个正整数的整数倍。
cnt = 0
for i in range(2, 2023 // 2 + 1):
    if 2023 % i == 0:
        print(str(i) + ",")
        cnt += 1
print(cnt + 2)
