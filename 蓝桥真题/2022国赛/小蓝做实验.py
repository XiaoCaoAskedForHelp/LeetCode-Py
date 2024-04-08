# with open("primes.txt", 'r') as fp:
#     data = fp.readlines()
# data1 = [int(i) for i in data if len(i) <= 9]  # 还有换行符需要多加1
# data2 = [int(i) for i in data if len(i) > 9]
# total = 10 ** 8 + 1
# is_prime = [True for _ in range(total)]
# primes = []
# for i in range(2, total):
#     if is_prime[i]:
#         primes.append(i)
#         for j in range(i * i, total, i):
#             is_prime[j] = False
# print(len(primes))
# count = 0
# # 统计10 的 8次方以下有多少素数
# for i in data1:
#     if is_prime[i]:
#         count += 1
# print(count)
# # 统计10 的8次方以上有多少素数
# flag = True
# for i in data2:
#     for j in range(2, int(i ** 0.5) + 1):  # 遍历可能的因子
#         if i % j == 0:
#             flag = False
#             break
#     if flag:
#         count += 1
#     flag = True
# print(count)

print(342693)