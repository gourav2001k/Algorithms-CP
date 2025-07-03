# https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/description/

class Solution:
    def kthCharacter(self, k: int) -> str:
        arr = [0]
        while len(arr) < k:
            for i in range(len(arr)):
                arr.append((arr[i]+1) % 26)
        return chr(arr[k-1]+97)
