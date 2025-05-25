# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/description/

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        c = Counter(words)
        out, same = 0, 0
        for x in c:
            if x == x[::-1]:
                if c[x] & 1:
                    same = 1
                    out += c[x] ^ 1
                else:
                    out += c[x]
            elif x[::-1] in c:
                out += min(c[x], c[x[::-1]])
        return 2*(out+same)
