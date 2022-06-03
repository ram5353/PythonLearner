from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1



    def maxDepthUsingBFS(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        q = deque([root])
        tree = [root.val]
        level = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    tree.append(node.left.val)
                if node.right:
                    q.append(node.right)
                    tree.append(node.right.val)
            level += 1
        print(tree)
        return level


    def maxDepthUsingIterativeDFS(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        result = 1
        while stack:
            node, depth = stack.pop()
            if node:
                result = max(result, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return result







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
print(s.maxDepthUsingBFS(root))
print(s.maxDepthUsingIterativeDFS(root))