# https://leetcode.com/problems/finding-3-digit-even-numbers/description/

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digits = Counter(digits)
        uniq = set()
        for i in range(1, 10):
            for j in range(10):
                for k in range(0, 10, 2):
                    c = Counter([i, j, k])
                    for x in c:
                        if digits[x] < c[x]:
                            break
                    else:
                        uniq.add(k+10*j+100*i)
        out = sorted(list(uniq))
        return out
