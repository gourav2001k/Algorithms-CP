# https://leetcode.com/problems/partition-labels/description/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        count = defaultdict(list)
        for i in range(n):
            count[s[i]].append(i)
        for x in count:
            count[x].reverse()

        out = []
        curSet, c = set(), 0
        for i in range(n):
            c += 1
            count[s[i]].pop()
            curSet.add(s[i])
            if not len(count[s[i]]):
                curSet.remove(s[i])
            if not curSet:
                out.append(c)
                c = 0
        return out
