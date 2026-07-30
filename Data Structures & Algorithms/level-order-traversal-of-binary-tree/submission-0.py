# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [[root]]
        result = []
        while len(queue):
            curr_level = queue.pop(0)
            nxt_level = []
            lvl_res = []
            while len(curr_level):
                curr_node = curr_level.pop(0)
                lvl_res.append(curr_node.val)
                if curr_node.left:
                    nxt_level.append(curr_node.left)
                if curr_node.right:
                    nxt_level.append(curr_node.right)
            # fill
            result.append(lvl_res)
            if len(nxt_level):
                queue.append(nxt_level)
        return result