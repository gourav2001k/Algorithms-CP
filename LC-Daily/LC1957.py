# https://leetcode.com/problems/delete-characters-to-make-fancy-string/description

class Solution:
    def makeFancyString(self, s: str) -> str:
        out = ''
        for i in s:
            if out[-2:] == i*2:
                continue
            out += i
        return out
