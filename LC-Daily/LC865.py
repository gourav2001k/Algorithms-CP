# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.subtreeWithAllDeepestHelper(root)[1]

    def subtreeWithAllDeepestHelper(self, root, level=0):
        if not root:
            return -1, None
        d1, ans1 = self.subtreeWithAllDeepestHelper(root.left, level+1)
        d2, ans2 = self.subtreeWithAllDeepestHelper(root.right, level+1)
        if d1 == d2:
            return max(d1, level), root
        if d1 > d2:
            return d1, ans1
        return d2, ans2
