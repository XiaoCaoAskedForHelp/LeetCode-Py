class Solution:
    # 将所有的子串按照其末尾字符的下标划分
    # 以s[i]结尾的子串，可以看成是以是s[i-1]结尾的子串，在末尾加上s[i]组成
    # 如果s[i]之前没有遇到过，子串的所有引力值都会增加1，在加上1，它本身,增加量为i+1
    # 如果s[i]之前遇到过，假设出现的下标为j，那么只有j + 1到i-1的子串的引力值会增加1，即增加i - j -1 在加上1，它本身
    # 用一个变量sums维护s[i]结尾的子串的引力值之和，通过用数组或者哈希记录每一个字符上次出现的下标，累加sums纪委答案
    def appealSum(self, s: str) -> int:
        ans, sums, last = 0, 0, {}
        for i, c in enumerate(s):
            sums += i - last.get(c, -1)  # 以i为结尾的所有子串就算完了,通过前一个sums进行递推计算 ，默认值设置为-1，是为了将两种情况进行合并
            ans += sums
            last[c] = i
        return ans
