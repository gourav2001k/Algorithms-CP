# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        mod = 10**9+7
        s = self.maxProductHelper(root)[0]
        return self.maxProductHelper(root, s)[1] % mod

    def maxProductHelper(self, root, total=0):
        if not root:
            return 0, 0
        s1, ans1 = self.maxProductHelper(root.left, total)
        s2, ans2 = self.maxProductHelper(root.right, total)
        out = max(ans1, ans2, s1*s2)
        treeSum = s1+s2+root.val
        out = max(out, treeSum*(total-treeSum))
        return treeSum, out
