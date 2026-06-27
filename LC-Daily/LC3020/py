# https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/description/

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count = Counter(nums)
        c = count[1]  # one count
        if not c & 1:
            c -= 1  # odd one count
        out = max(1, c)
        for x in count:
            if x == 1:
                continue
            c, l = x, 1
            while count[c] > 1 and count[c**2]:
                l += 2
                c *= c
            out = max(out, l)
        return out
