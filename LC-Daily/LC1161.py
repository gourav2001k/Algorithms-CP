# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        out = -10**5
        bestLevel, level = 1, 0
        while q:
            level += 1
            curSum = 0
            for x in range(len(q)):
                cur = q.popleft()
                curSum += cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            if curSum > out:
                bestLevel = level
                out = curSum
        return bestLevel
