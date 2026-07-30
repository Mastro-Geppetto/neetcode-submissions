# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ele = []
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            self.ele.append(root.val)
            self.inorder(root.right)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        # O(n)
        self.inorder(root)
        # O(nlogn)
        sorted_list = sorted(set(self.ele))
        print(self.ele, sorted_list)
        if sorted_list == self.ele:
            return True
        return False