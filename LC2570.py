# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/description/

class Solution:
    def mergeArrays(self, arr1: List[List[int]], arr2: List[List[int]]) -> List[List[int]]:
        n, m = len(arr1), len(arr2)
        out = []

        i, j = 0, 0
        while i < n and j < m:
            if arr1[i][0] < arr2[j][0]:
                out.append(arr1[i])
                i += 1
            elif arr1[i][0] > arr2[j][0]:
                out.append(arr2[j])
                j += 1
            else:
                out.append([arr1[i][0], arr1[i][1]+arr2[j][1]])
                i += 1
                j += 1

        while i < n:
            out.append(arr1[i])
            i += 1

        while j < m:
            out.append(arr2[j])
            j += 1

        return out
