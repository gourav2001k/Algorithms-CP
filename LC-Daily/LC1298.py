# https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/description/

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(keys)
        avail = set()
        take = deque()
        for x in initialBoxes:
            if status[x]:
                take.append(x)
            else:
                avail.add(x)

        out = 0
        while take:
            x = take.popleft()
            out += candies[x]
            for k in containedBoxes[x]:
                if status[k]:
                    take.append(k)
                else:
                    avail.add(k)
            for k in keys[x]:
                status[k] = 1
                if k in avail:
                    avail.remove(k)
                    take.append(k)
        return out
