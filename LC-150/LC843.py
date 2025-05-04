# https://leetcode.com/problems/guess-the-word/description/

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        match = 0
        while match != 6:
            guess = words[randint(0, len(words)-1)]
            match = master.guess(guess)
            if match == 6:
                break
            words = self.filter(words, guess, match)

    def filter(self, words, word, m):
        candidates = []
        for candidate in words:
            if candidate == word:
                continue
            c = 0
            for i in range(6):
                if word[i] == candidate[i]:
                    c += 1
            if c == m:
                candidates.append(candidate)
        return candidates
