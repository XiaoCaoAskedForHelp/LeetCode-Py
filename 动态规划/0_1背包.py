def package01(weight: list, value: list, bagweight: int) -> int:
    # 二维数组
    dp = [[0] * (bagweight + 1) for _ in range(len(weight))]

    # 初始化
    for j in range(weight[0], bagweight + 1):
        dp[0][j] = value[0]

    # weight数组的大小就是物品的数量
    for i in range(1, len(weight)):  # 遍历物品
        for j in range(1, bagweight + 1):
            if j < weight[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])
    return dp[len(weight) - 1][bagweight]


if __name__ == "__main__":
    weight = [1, 3, 4]
    value = [15, 20, 30]
    bagweight = 4

    result = package01(weight, value, bagweight)
    print(result)
