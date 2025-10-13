# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/description

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        stack = []
        for idx, word in enumerate(words):
            x = "".join(sorted(list(word)))
            if stack and x == stack[-1][0]:
                continue
            stack.append((x, idx))
        out = []
        while stack:
            x, i = stack.pop()
            out.append(words[i])
        return out[::-1]
