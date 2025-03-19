# https://leetcode.com/problems/maximum-product-subarray/description/

class Solution:
    def maxProduct(self, arr: List[int]) -> int:
        n = len(arr)
        out, cur = arr[0], 1
        neg, negV = -1, 1
        for i in range(n):
            cur *= arr[i]
            # potential ans, cur product
            # and if prod negative use first neg(after last 0) ,to make it postive
            out = max(out, cur, cur//negV)
            if cur < 0 and neg == -1:
                #  when first neg after 0 found store it
                neg, negV = i, cur
            if cur == 0:
                # when 0 found reset the results
                cur = 1
                neg, negV = -1, 1
        return out
