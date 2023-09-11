def test_1_wei_bag_problem(weight, value, bagWeight):
    # 初始化
    dp = [0] * (bagWeight + 1)

    for i in range(len(weight)):  # 遍历物品
        for j in range(bagWeight,weight[i] - 1, -1): # 遍历背包容量
            dp[j] = max(dp[j], dp[j-weight[i]] + value[i])

    return dp[bagWeight]

if __name__ == "__main__":

    weight = [1, 3, 4]
    value = [15, 20, 30]
    bagweight = 4

    result = test_1_wei_bag_problem(weight, value, bagweight)
    print(result)