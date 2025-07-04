# https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/description/

class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        b = 1
        while (1 << b) < k:
            b += 1

        def find(b, k):
            b -= 1
            if b < 0:
                return 0
            s = 1 << b
            if k > s:
                k -= s
                x = find(b, k)
                if operations[b] == 1:
                    return (x+1) % 26
                return x
            return find(b, k)

        return chr(97+find(b, k))
