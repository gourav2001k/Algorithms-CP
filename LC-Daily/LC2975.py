# https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/description/

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        mod = 10**9+7
        hFences = hFences+[1, m]
        vFences = vFences+[1, n]
        hFences.sort()
        vFences.sort()

        def allPossibleLengths(arr):
            l = len(arr)
            deltas = []
            for i in range(1, l):
                deltas.append(arr[i]-arr[i-1])
            lengths = set()
            for i in range(l-1):
                t = 0
                for j in range(i, l-1):
                    t += deltas[j]
                    lengths.add(t)
            return lengths

        hLengths = allPossibleLengths(hFences)
        vLengths = allPossibleLengths(vFences)
        ans = hLengths.intersection(vLengths)
        if not ans:
            return -1
        return (max(ans)**2) % mod
