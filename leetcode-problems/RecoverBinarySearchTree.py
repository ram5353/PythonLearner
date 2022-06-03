from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]):
        self.temp = []
        def fn(node):
            if not node: return
            fn(node.left)
            self.temp.append(node)
            fn(node.right)

        fn(root)
        str = sorted(n.val for n in self.temp)
        for i in range(len(str)):
            self.temp[i].val = str[i]


s = Solution()
t = TreeNode()
l = TreeNode()
r = TreeNode()
r.val = 2
l.val = 3
t.val = 1
t.left = l
l.right = r
print(s.recoverTree(t))
