# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.comm_root = None
    def locate(self, root, a, b ):
        if not root:
            return TreeNode()
        if root.val > a.val and root.val > b.val:
            # go HARD left
            return self.locate(root.left, a, b)
        elif root.val < a.val and root.val < b.val:
            # go HARD right
            return self.locate(root.right, a, b)
        else:
            if root.val == a.val or root.val == b.val:
                self.comm_root = root
            return root

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self.locate(root, p, q)