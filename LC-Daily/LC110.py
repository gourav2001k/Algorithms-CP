# https://leetcode.com/problems/balanced-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def solve(root):
            if not root:
                return True, 0
            p1, l = solve(root.left)
            p2, r = solve(root.right)
            if not (p1 and p2):
                return False, -1
            if abs(l-r) > 1:
                return False, -1
            return True, max(l, r)+1
        return solve(root)[0]
