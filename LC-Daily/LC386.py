# https://leetcode.com/problems/lexicographical-numbers/description/

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def getNum(cur):
            out = 0
            for i in cur:
                out *= 10
                out += i
            return out

        def next(cur):
            cur.append(0)
            x = getNum(cur)
            if x <= n:
                return [x]+next(cur)
            cur.pop()
            for i in range(len(cur)-1, -1, -1):
                if cur[i] < 9:
                    cur[i] += 1
                    x = getNum(cur)
                    if x <= n:
                        return [x]+next(cur)
                    else:
                        cur.pop()
                else:
                    cur.pop()
            return []

        return [1]+next([1])
