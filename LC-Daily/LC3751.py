# https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/description/

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        out = 0
        for x in range(num1, num2+1):
            out += self.countWavy(x)
        return out

    def countWavy(self, x):
        k = 0
        arr = list(map(int, list(str(x))))
        for i in range(1, len(arr)-1):
            if arr[i-1] < arr[i] > arr[i+1]:
                k += 1
            elif arr[i-1] > arr[i] < arr[i+1]:
                k += 1
        return k
