# https://leetcode.com/problems/partition-array-according-to-given-pivot/description/

class Solution:
    def pivotArray(self, arr: List[int], pivot: int) -> List[int]:
        a, b, c = [], [], []
        for i in arr:
            if i < pivot:
                a.append(i)
            elif i > pivot:
                c.append(i)
            else:
                b.append(i)
        return a+b+c
