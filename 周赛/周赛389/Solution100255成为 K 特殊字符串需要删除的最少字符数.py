from cmath import inf


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        words = [0] * 26
        for w in word:
            words[ord(w) - ord('a')] += 1
        words = [i for i in words if i != 0]
        words.sort()
        words.reverse()
        # 只能删除
        record = [0] * len(words)
        for i in range(1, len(words)):
            tmp = 0
            for j in range(0, i):
                if abs(words[i] - words[j]) > k:
                    tmp += abs(words[i] - words[j]) - k
            record[i] = tmp

        cnt = record[-1]
        for j in range(len(words) - 1, -1, -1):
            tmp = sum(words[j:])
            if tmp > cnt:
                break
            else:
                cnt = min(cnt, tmp + record[j - 1])

        return cnt

    def minimumDeletions1(self, word: str, k: int) -> int:
        words = [0] * 26
        for i in word:
            words[ord(i) - ord('a')] += 1
        ans = inf
        for i in range(26):
            cur = 0
            # 因为只能删除，所以比words[i]小的都不要，比words[i] + k大的就要减小
            for j in range(26):
                if words[j] > words[i] + k:
                    cur += (words[j] - words[i] - k)
                elif words[j] < words[i]:
                    cur += words[j]
            ans = min(ans, cur)
        return ans


Solution().minimumDeletions1(word="vvnowvov", k=2)
