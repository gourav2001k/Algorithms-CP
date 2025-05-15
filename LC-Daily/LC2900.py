# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/description/
class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n, out = len(words), [0]
        for i in range(1, n):
            if groups[out[-1]] != groups[i]:
                out.append(i)
        return [words[i] for i in out]
