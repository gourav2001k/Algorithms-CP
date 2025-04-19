# https://leetcode.com/problems/rabbits-in-forest/description

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        out = 0
        for x in count:
            out += ceil(count[x]/(x+1))*(x+1)
        return out
