# https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/description

class Solution:
    def minMaxDifference(self, n: int) -> int:
        s = str(n)
        mx, mn = '', ''
        a, b = '', ''
        for i in s:
            if not mx and i != '9':
                mx = i
            if not mn:
                mn = i
            if mx and mx == i:
                a += '9'
            else:
                a += i
            if mn and mn == i:
                b += '0'
            else:
                b += i

        return int(a)-int(b)
