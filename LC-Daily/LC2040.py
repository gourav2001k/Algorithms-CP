# https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/description/

class Solution:
    def kthSmallestProduct(self, arr1: List[int], arr2: List[int], k: int) -> int:
        z, n = 0, len(arr2)
        negs, pos = [], []
        for i in arr2:
            if i < 0:
                negs.append(-i)
            elif i > 0:
                pos.append(i)
            else:
                z += 1
        negs.reverse()

        def count(x, l):
            if x == 0:
                if l >= 0:
                    return n
                else:
                    return 0

            out = 0
            if l >= 0 and x > 0:
                out += len(negs)
                out += bisect_right(pos, l//x)
                out += z
                return out
            if l >= 0 and x < 0:
                out += len(pos)
                out += bisect_right(negs, l//-x)
                out += z
                return out
            l *= -1
            if x > 0:
                q = l//x
                if l % x:
                    q += 1
                out += len(negs)-bisect_left(negs, q)
                return out
            else:
                q = l//-x
                if l % (-x):
                    q += 1
                out += len(pos)-bisect_left(pos, q)
                return out

        def greaterThanKElements(x):
            out = 0
            for i in arr1:
                out += count(i, x)
                # print(i,x,out)
            # print(x,out)
            return out >= k

        l, r = -10**12, 10**12
        while l+1 < r:
            m = (l+r) >> 1
            if greaterThanKElements(m):
                r = m
            else:
                l = m
        return r
