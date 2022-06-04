import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: Optional[TreeNode]):
    if not root:
        return []
    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)


def isValidBST(root: Optional[TreeNode]):
    def inorder(root):
        if not root:
            return True
        if not inorder(root.left):
            return False
        if root.val <= prev:
            return False
        prev = root.val
        return inorder(root.right)

    prev = -math.inf
    inorder(root)



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
print(inorderTraversal(root))


