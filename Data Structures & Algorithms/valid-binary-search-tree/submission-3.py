# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def check(self, root, left_lmt, right_lmt):
        if not root:
            return True
        print(root.val, left_lmt, right_lmt)
        if root.val <= left_lmt or root.val >= right_lmt:
            return False
        return self.check(root.left, left_lmt, root.val) and\
               self.check(root.right,root.val, right_lmt)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check(root, -1001, 1001)