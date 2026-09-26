# https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/description/

class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        pairs = dict()
        for a, b in knowledge:
            pairs[a] = b

        out, cur = '', ''
        for x in s:
            if x == ')':
                if cur[1:] in pairs:
                    out += pairs[cur[1:]]
                else:
                    out += '?'
                cur = ''
            elif x == '(' or cur:
                cur += x
            else:
                out += x
        return out
