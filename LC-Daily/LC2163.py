# https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/

class Solution:
    def minimumDifference(self, arr: List[int]) -> int:
        n = len(arr)//3

        maxHeap = [-arr[i] for i in range(n)]
        minHeap = [arr[-i-1] for i in range(n)]
        heapify(maxHeap)
        heapify(minHeap)

        curLeft, curRight = -sum(maxHeap), sum(minHeap)
        left, right = [curLeft], [curRight]
        for i in range(n, 2*n):
            if -maxHeap[0] > arr[i]:
                curLeft += heappushpop(maxHeap, -arr[i])
                curLeft += arr[i]
            if minHeap[0] < arr[-1-i]:
                curRight -= heappushpop(minHeap, arr[-1-i])
                curRight += arr[-1-i]
            left.append(min(curLeft, left[-1]))
            right.append(max(curRight, right[-1]))
        right.reverse()

        out = sum(arr)
        for i in range(n+1):
            out = min(out, left[i]-right[i])
        return out
