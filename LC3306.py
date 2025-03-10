# https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/description

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def minK(x):
            n = len(word)
            vowels = 'aeiou'
            vLoc = [-1, -1, -1, -1, -1]
            out = 0
            l, c = 0, 0
            for i in range(n):
                if word[i] in vowels:
                    vLoc[vowels.index(word[i])] = i
                else:
                    c += 1
                while c >= x and min(vLoc) != -1:
                    out += n-i
                    if word[l] in vowels:
                        if vLoc[vowels.index(word[l])] == l:
                            vLoc[vowels.index(word[l])] = -1
                    else:
                        c -= 1
                    l += 1
            return out

        return minK(k)-minK(k+1)
