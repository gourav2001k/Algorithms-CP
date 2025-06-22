# https://leetcode.com/problems/divide-a-string-into-groups-of-size-k

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        out, n = [], len(s)
        for i in range(0, n, k):
            out.append(s[i:i+k])
        out[-1] += (k-len(out[-1]))*fill
        return out
