# https://leetcode.com/problems/divide-array-into-equal-pairs/description

class Solution:
    def divideArray(self, arr: List[int]) -> bool:
        c = Counter(arr)
        for x in c:
            if c[x] & 1:
                return False
        return True
