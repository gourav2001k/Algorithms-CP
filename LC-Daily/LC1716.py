# https://leetcode.com/problems/calculate-money-in-leetcode-bank/description

class Solution:
    def totalMoney(self, n: int) -> int:
        val = [1, 2, 3, 4, 5, 6]
        s = 1+2+3+4+5+6+7
        c = n//7
        return (c*(2*s+(c-1)*7))//2 + sum(val[:n % 7]) + (n % 7)*c
