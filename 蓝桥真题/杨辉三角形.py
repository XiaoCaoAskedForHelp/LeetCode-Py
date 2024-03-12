# 组合数
# 如果该斜行最小元素都已经超出10的9次方那么剩下的元素都是大于10的9次方的，
# 也就是说这一斜行是没有意义的，不用考虑。经计算，只有16斜行以内的数才符合条件。

# 斜行同样可以用组合数表示。从全是1的最外层元素开始数（假设是第0斜行），
# 则第 i 斜行的元素可以用组合数C(i, P)表示(P >= 2i，因为斜行的第一个元素就是C(i，2i)，见性质2。
# 因此，斜行中每往下一个元素P就加1,i不变）。
# 因为相同斜行的组合数上限不变，我们不断更换组合数下限的值，直到最后找到目标值即可。
target = int(input())


def C(a, b):  # a为上限，b为下限
    res = 1
    for _ in range(a):
        res *= b / a  # 除下来是小数
        if res > target:
            return res
        b -= 1
        a -= 1
    return int(res)


# 二分查找目标元素
# 组合数上标是斜行的行数，下标是正行的行数
def search(k: int):  # k是斜行的下标是固定的，有序的,作为组合数的上标
    # 起始下限，也就是对称轴上的元素
    low = 2 * k
    # 终点下限
    high = target
    while low <= high:
        mid = (low + high) // 2
        val = C(k, mid)
        if val > target:
            high = mid - 1
        elif val < target:
            low = mid + 1
        else:
            print(mid * (mid + 1) // 2 + k + 1)
            return True
    return False


# print(int(C(16, 32))) # 601080390   所以只需要搜索到第16个斜行
# print(int(C(17, 34))) # 2333606220

# 要倒着搜索斜行，下标为1的斜行兜底是一定能搜到的，C（1，target）
for i in range(16, -1, -1):
    if search(i):
        break
