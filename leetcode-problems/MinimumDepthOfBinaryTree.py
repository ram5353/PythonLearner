# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            children = [node.left, node.right]
            if not any(children):
                return depth
            for c in children:
                if c:
                    queue.append((c, depth + 1))

    def minDepthUsingUsingDFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [root, 1]
        min_depth = float('inf')
        while stack:
            node, depth = stack.pop()
            children = [node.left, node.right]
            if not any(children):
                min_depth = min(depth, min_depth)
            for c in children:
                if c:
                    stack.append((c, depth + 1))

        return min_depth

