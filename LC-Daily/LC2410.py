# https://leetcode.com/problems/maximum-matching-of-players-with-trainers/description/

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        n, m = len(players), len(trainers)
        players.sort()
        trainers.sort()
        i, j = 0, 0
        while i < n and j < m:
            if players[i] <= trainers[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i
