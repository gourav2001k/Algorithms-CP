# https://leetcode.com/problems/count-largest-group/description/

class Solution:
    def countLargestGroup(self, n: int) -> int:
        group = Counter()
        mex = 0
        for x in range(1, n+1):
            c = 0
            while x:
                c += x % 10
                x //= 10
            group[c] += 1
            mex = max(group[c], mex)

        return list(group.values()).count(mex)
