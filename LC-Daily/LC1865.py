# https://leetcode.com/problems/finding-pairs-with-a-certain-sum/description/

class FindSumPairs:

    def __init__(self, arr1: List[int], arr2: List[int]):
        self.arr1 = arr1
        self.arr2 = arr2
        self.cnt = Counter(arr2)

    def add(self, idx: int, val: int) -> None:
        self.cnt[self.arr2[idx]] -= 1
        self.arr2[idx] += val
        self.cnt[self.arr2[idx]] += 1

    def count(self, tot: int) -> int:
        out = 0
        for i in self.arr1:
            out += self.cnt[tot-i]
        return out


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
