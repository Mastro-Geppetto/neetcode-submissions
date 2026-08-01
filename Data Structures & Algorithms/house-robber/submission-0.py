class Solution:
    '''
Like "climbing stairs", we select next step +2 or +3 +4..
    Suppose we start from left, dfs solution will be -
    indexes travarsal
        [0]->[2 or 3 or ...]->[prev+2 or or ...]->last cell
    We can dfs, returining sums of path.
    but without Memoization it will time out

    def pure_bfs(nums, i):
        if len(nuns) > 2:
          return max( dfs(num, 0), dfs(nums, 1) )
    where
        dfs(num, i)
            if i >= len(num)
                return 0
            max_sum = 0
            for j in range(i+2, len(nums))
                max_sum = max(
                            max_sum,
                            nums[i] + bfs(nums, j)
                            )
            return max(max_sum, nums[i])
'''

    def __init__(self) -> None:
        self.cache = []

    def dfs(self, nums, i):
        #print(f"d: i:{i}={nums[i]}")
        if i >= len(nums):
            return 0
        if self.cache[i] != -1:
            return self.cache[i]
        max_sum = 0
        # select next
        for j in range(i+2,len(nums)):
            max_sum = max(max_sum, nums[i] + self.dfs(nums, j))
            #print(f"\td:({i},{j}):sum:{max_sum}")
        #print(f"\td:({i}):ret:{max(max_sum, nums[i])}")
        self.cache[i] = max(max_sum, nums[i])
        return self.cache[i]

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        self.cache = [-1]*(len(nums)+1)
        return max(
            self.dfs(nums, 0),
            self.dfs(nums, 1))