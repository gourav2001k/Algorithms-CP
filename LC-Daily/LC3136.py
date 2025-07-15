# https://leetcode.com/problems/valid-word/description

class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        if not word.isalnum():
            return False
        vowels = set({'a', 'e', 'i', 'o', 'u'})
        v, c = 0, 0
        for i in word:
            if i.isdigit():
                continue
            if i.lower() in vowels:
                v += 1
            else:
                c += 1
        if v and c:
            return True
        return False
