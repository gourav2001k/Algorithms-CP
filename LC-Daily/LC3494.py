# https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/description/

class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        times = [0 for i in range(n+1)]
        for m in mana:
            for i in range(n):
                times[i+1] = max(times[i], times[i+1])+m*skill[i]
            for i in range(n-1, -1, -1):
                times[i] = times[i+1]-m*skill[i]
        return times[n]
