# https://leetcode.com/problems/fraction-to-recurring-decimal/description/

class Solution:
    def fractionToDecimal(self, num: int, deno: int) -> str:
        out = ''
        if deno < 0:
            num *= -1
            deno *= -1
        if num < 0:
            out = '-'
        num = abs(num)
        if num >= deno:
            out += str(num//deno)
        else:
            out += '0'
        num %= deno
        if not num:
            return out
        else:
            out += '.'

        decimal, idx = '', 0
        encountered = dict()
        while num and num not in encountered:
            encountered[num] = idx
            idx += 1
            num *= 10
            decimal += str(num//deno)
            num %= deno

        if num:
            out += decimal[:encountered[num]] + \
                '('+decimal[encountered[num]:]+')'
        else:
            out += decimal
        return out
