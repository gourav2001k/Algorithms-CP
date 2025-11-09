# https://leetcode.com/problems/count-days-without-meetings/description/

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        prev, out = 1, 0
        for a, b in meetings:
            if prev < a:
                out += a-prev
            prev = max(b+1, prev)
        out += days-prev+1
        return out
