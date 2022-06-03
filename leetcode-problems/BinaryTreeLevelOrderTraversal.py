from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]):
        level = 0
        levels = []
        if not root:
            return levels
        q = deque([root])
        while q:
            levels.append([])
            level_length = len(q)
            for i in range(level_length):
                node = q.popleft()
                levels[level].append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return levels




root = TreeNode()
l_9 = TreeNode()
r_20 = TreeNode()
l_15 = TreeNode()
r_7 = TreeNode()
r_7.val = 7
l_15.val = 15
l_9.val = 9
r_20.val = 20
root.val = 3
root.left = l_9
root.right = r_20
r_20.left = l_15
r_20.right = r_7
s = Solution()
print(s.levelOrder(root))