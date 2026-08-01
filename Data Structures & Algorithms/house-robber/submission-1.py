class Solution:
    def __init__(self):
        self.cache = []

    def dfs(self, nums:List[int], i:int) -> int:
        if i >= len(nums):
            return 0
        # we start from next or we pick current + next2next
        if self.cache[i] != -1:
            return self.cache[i]
        self.cache[i] = \
            max(
                self.dfs(nums, i + 1),
                (nums[i] + self.dfs(nums, i + 2))
            )
        return self.cache[i]

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        # cache
        self.cache = [-1]*(len(nums)+1)
        # dfs
        return self.dfs(nums, 0)
        