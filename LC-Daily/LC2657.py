# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/description/?

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        out = [0]
        setA, setB = set(), set()
        for i in range(n):
            setA.add(A[i])
            setB.add(B[i])
            out.append(out[i])
            if A[i] == B[i]:
                out[i+1] += 1
            else:
                if A[i] in setB:
                    out[i+1] += 1
                if B[i] in setA:
                    out[i+1] += 1
        return out[1:]
