# Problem Link: https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        n = len(traversal)
        cur = traversal[0]
        seq = []  # to extract the numeric node values and heights
        for i in range(1, n):
            if traversal[i].isdigit():
                if cur[-1] == '-':
                    seq.append(len(cur))
                    cur = ''
            else:
                if cur[-1].isdigit():
                    seq.append(int(cur))
                    cur = ''
            cur += traversal[i]
        seq.append(int(cur))

        # Stack to keep track of the mimic DFS
        out = TreeNode(seq[0])
        stack, d = [out], 0
        for i in range(1, len(seq), 2):
            h, v = seq[i], seq[i+1]
            # adjusting current depth to parent level of next node
            while d >= h:
                stack.pop()
                d -= 1
            # try to fix the left node
            if not stack[-1].left:
                stack[-1].left = TreeNode(v)
                stack.append(stack[-1].left)
                d += 1
            else:  # otherwise right
                stack[-1].right = TreeNode(v)
                stack.append(stack[-1].right)
                d += 1

        return out
