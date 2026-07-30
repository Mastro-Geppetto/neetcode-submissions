class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = sum(nums)
        n = len(nums)
        expectedSum = (n*(n+1))/2
        return int(expectedSum - s)