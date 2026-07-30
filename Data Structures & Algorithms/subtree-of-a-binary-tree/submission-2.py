# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def comp_sub_tree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if (not root and subRoot) or (root and not subRoot):
            return False
        if not root and not subRoot:
            return True
        if root.val != subRoot.val:
            return False
        return self.comp_sub_tree(root.left,  subRoot.left) and\
               self.comp_sub_tree(root.right, subRoot.right)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Duplicate values are present
        if root:
            if root.val == subRoot.val and\
               self.comp_sub_tree(root, subRoot):
               return True
            return self.isSubtree(root.left,  subRoot) or\
                   self.isSubtree(root.right, subRoot)
        return False

