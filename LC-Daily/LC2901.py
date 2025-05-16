# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/description/

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        # length,prev
        dp = [[1, i] for i in range(n)]
        mx, idx = 1, 0
        for i in range(1, n):
            for j in range(i):
                if len(words[i]) != len(words[j]):
                    continue
                if dp[j][0]+1 <= dp[i][0]:
                    continue
                if groups[i] == groups[j]:
                    continue
                if self.hammingD(words[i], words[j]) != 1:
                    continue
                dp[i] = [dp[j][0]+1, j]
                if dp[i][0] > mx:
                    mx, idx = dp[i][0], i

        out = []
        while dp[idx][1] != idx:
            out.append(words[idx])
            idx = dp[idx][1]
        out.append(words[idx])
        out.reverse()
        return out

    def hammingD(self, word1, word2):
        n = len(word1)
        out = 0
        for i in range(n):
            out += word1[i] != word2[i]
        return out
