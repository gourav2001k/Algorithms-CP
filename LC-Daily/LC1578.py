# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/description/

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        color, temp = "", []
        out = 0
        for i in range(n):
            if not color:
                color = colors[i]
                temp.append(neededTime[i])
            elif color != colors[i]:
                out += sum(temp)-max(temp)
                color = colors[i]
                temp = [neededTime[i]]
            else:
                temp.append(neededTime[i])
        out += sum(temp)-max(temp)
        return out
