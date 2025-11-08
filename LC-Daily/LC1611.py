# https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/description/

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if not n:
            return 0
        cur, mex = n, 0
        while cur:
            cur >>= 1
            mex += 1
        return (1 << mex)-1-self.minimumOneBitOperations(n ^ (1 << (mex-1)))
