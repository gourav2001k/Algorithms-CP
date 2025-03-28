# https://leetcode.com/problems/random-pick-with-weight/description/

class Solution:

    def __init__(self, w: List[int]):
        s = sum(w)
        self.n = len(w)
        self.probs = []
        for i in range(self.n):
            p = w[i]/s
            self.probs.append([p, w[i], i])
        self.probs.sort()
        for i in range(1, self.n):
            self.probs[i][0] += self.probs[i-1][0]

    def pickIndex(self) -> int:
        p = uniform(0, 1)
        idx = bisect_left(self.probs, [p, 10**9])
        return self.probs[idx][2]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
