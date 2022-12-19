class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode):
        result = []
        if root is None:
            return []
        result = self.inorderTraversal(root.left)
        result.append(root.val)
        result = result + self.inorderTraversal(root.right)
        return result

    def isSameTree(self, p: TreeNode, q: TreeNode):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
    def isSymmetric(self, root: TreeNode):
        if not root:
            return False
        def result(left, right):
            if not left and not right:
                return True
            if not left or not right or left.val != right.val:
                return False
            return result(left.left, right.right) and result(left.right, right.left)
        return result(root.left, root.right)
        
r = TreeNode(10)
left = TreeNode(3)
right = TreeNode(3)
r.left = left
r.right = right

m = TreeNode(10)
left = TreeNode(3)
right = TreeNode(5)
m.left = left
m.right = right

s = Solution()
print(s.inorderTraversal(r))
print(s.isSameTree(r,m))
print(s.isSymmetric(r))
