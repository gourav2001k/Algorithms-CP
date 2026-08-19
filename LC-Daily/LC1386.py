# https://leetcode.com/problems/cinema-seat-allocation/description/

class Solution:
    def maxNumberOfFamilies(self, n: int, seats: List[List[int]]) -> int:
        out = n*2
        occ = defaultdict(list)
        for x, y in seats:
            occ[x].append(y)

        for row in occ:
            a, b, c = 1, 1, 1
            for x in occ[row]:
                if 2 <= x <= 5:
                    a = 0
                if 4 <= x <= 7:
                    b = 0
                if 6 <= x <= 9:
                    c = 0
            out += max(a+c, b)-2
        return out
