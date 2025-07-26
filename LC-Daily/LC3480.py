# https://leetcode.com/problems/maximize-subarrays-after-removing-one-conflicting-pair/description

class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        right = [[] for i in range(n+1)]
        for a, b in conflictingPairs:
            right[max(a, b)].append(min(a, b))

        out = 0
        l1, l2 = 0, 0
        diff = [0 for i in range(n+1)]
        for r in range(1, n+1):
            for l in right[r]:
                if l > l1:
                    l1, l2 = l, l1
                elif l > l2:
                    l1, l2 = l1, l
            out += r-l1
            diff[l1] += l1-l2
        return out+max(diff)
