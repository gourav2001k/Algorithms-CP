# https://leetcode.com/problems/shortest-way-to-form-string/description/

class Solution:
    """
    @param s: Source string
    @param target: Target string
    @return: Number of subsequences that can be spliced into target
    """

    def shortest_way(self, src: str, target: str) -> int:
        # write your code here
        n, m = len(target), len(src)
        i, j = 0, 0
        res, k = 0, 0
        while i < n:
            while j < m and src[j] != target[i]:
                j += 1
            if j == m:
                if not k:
                    return -1  # target[i] doesn't exist in src
                res += 1  # src string exhausted
                j, k = 0, 0  # reinit src
            else:
                i += 1
                j += 1
                k += 1
        if k:
            res += 1
        return res
