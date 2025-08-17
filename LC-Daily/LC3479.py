# https://leetcode.com/problems/fruits-into-baskets-iii/description/

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        seg = SegTree(baskets)
        out, n = 0, len(baskets)
        for x in fruits:
            idx = self.findMinIdx(seg, n, x)
            if idx == -1:
                out += 1
            else:
                seg.update(idx, 0)
        return out

    def findMinIdx(self, seg, n, x):
        # seg.tree[1] stores ans of entire tree
        if seg.tree[1] < x:
            return -1
        l, r = 0, n
        while l+1 < r:
            m = (l+r) >> 1
            if seg.query(0, m) >= x:
                r = m
            else:
                l = m
        return r-1


class SegTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = arr+arr
        for i in range(self.n-1, 0, -1):
            self.tree[i] = max(self.tree[i << 1], self.tree[1+(i << 1)])

    def update(self, idx, x):
        # 0 based update
        idx += self.n
        self.tree[idx] = x
        while idx > 1:
            idx >>= 1
            self.tree[idx] = max(self.tree[idx << 1], self.tree[1+(idx << 1)])

    def query(self, l, r):
        # max of in [l,r)
        l += self.n
        r += self.n
        out = 0  # sample space has positive values
        while l < r:
            if l & 1:
                out = max(self.tree[l], out)
                l += 1
            if r & 1:
                r -= 1
                out = max(self.tree[r], out)
            l >>= 1
            r >>= 1
        return out
