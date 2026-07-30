class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = set(nums)
        return len(d) != len(nums)