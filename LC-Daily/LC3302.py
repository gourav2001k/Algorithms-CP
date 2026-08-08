# https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/description/

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n = len(word1)
        m = len(word2)
        suff = [0 for i in range(n)]
        j, l = m-1, 0
        for i in range(n-1, -1, -1):
            suff[i] = l
            if j >= 0 and word1[i] == word2[j]:
                l += 1
                j -= 1

        out = []
        j, used = 0, False
        for i in range(n):
            if word1[i] == word2[j]:
                out.append(i)
                j += 1
            elif not used and suff[i] >= m-j-1:
                used = True
                out.append(i)
                j += 1
            if j == m:
                return out
        return []
