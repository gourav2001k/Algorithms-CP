# Problem Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)

        def construct(i, j, x, y):
            if j < i:
                return
            root = TreeNode(preorder[i])
            if i == j:
                return root
            k = x
            while k <= y and postorder[k] != preorder[i+1]:
                k += 1
            if k <= y:
                root.left = construct(i+1, i+1+k-x, x, k)
                root.right = construct(i+k-x+2, j, k+1, j-1)
            else:
                root.right = construct(i+1, j, x, j-1)
            return root

        return construct(0, n-1, 0, n-1)
