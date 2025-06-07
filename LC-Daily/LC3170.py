# https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/description/

class Solution:
    def clearStars(self, s: str) -> str:
        n = len(s)
        count = defaultdict(list)

        def removeSmallest():
            for i in range(26):
                if count[chr(97+i)]:
                    count[chr(97+i)].pop()
                    break

        for i in range(n):
            if s[i] == "*":
                removeSmallest()
            else:
                count[s[i]].append(i)
        idxs = []
        for x in count:
            idxs += count[x]
        idxs.sort()
        return "".join(s[i] for i in idxs)
