# https://leetcode.com/problems/maximum-69-number/description/

class Solution:
    def maximum69Number(self, num: int) -> int:
        out, done = '', False
        for i in str(num):
            if i == '6' and not done:
                out += '9'
                done = True
            else:
                out += i
        return int(out)
