# https://leetcode.com/problems/type-of-triangle/description/

class Solution:
    def triangleType(self, arr: List[int]) -> str:
        arr.sort()
        if arr[0]+arr[1] <= arr[2]:
            return "none"
        if len(set(arr)) == 1:
            return "equilateral"
        if len(set(arr)) == 2:
            return "isosceles"
        return "scalene"
