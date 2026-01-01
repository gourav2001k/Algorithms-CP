# https://leetcode.com/problems/plus-one/description

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        digits.reverse()
        c = 1
        for i in range(n):
            c += digits[i]
            digits[i] = c % 10
            c = c//10
        if c:
            digits.append(c)
        digits.reverse()
        return digits
