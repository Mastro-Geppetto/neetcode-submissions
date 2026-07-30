# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self) -> None:
        self.max_till_now = -1001*1001
    def path_max_sum( self, root: Optional[TreeNode] )-> int:
        (left_sum,right_sum) = (-1001*1001, -1001*1001)
        if root.left:
            left_sum = self.path_max_sum( root.left )
        if root.right:
            right_sum= self.path_max_sum( root.right)
        # current sum = self + lft_sub_tree + rt_sub_tree
        curr_max_sum = max(  root.val,
                             root.val+left_sum,
                             root.val+right_sum,
                             root.val+left_sum+right_sum )
        self.max_till_now = max(self.max_till_now, curr_max_sum)
        print("at:", root.val, "max_sum:", curr_max_sum)
        # return max sum
        ret_max_sum = max(  root.val,
                            root.val+left_sum,
                            root.val+right_sum)
        return ret_max_sum
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        _ = self.path_max_sum(root)
        return self.max_till_now