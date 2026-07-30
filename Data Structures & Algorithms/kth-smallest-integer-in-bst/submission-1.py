# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self) -> None:
        self.result = -1
    def traverse(self, root, counter, k):
        ####
        if root.left:
            counter = self.traverse( root.left, counter, k )
        #
        counter += 1
        print(root.val, counter, k)
        if counter == k:
            self.result = root.val
        ####
        if root.right:
            counter = self.traverse( root.right, counter, k )
        return counter


    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        self.traverse(root, 0, k)
        return self.result