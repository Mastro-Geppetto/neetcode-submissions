class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l_idx = 0
        r_idx = len(numbers)-1
        while l_idx < r_idx:
            s = numbers[l_idx] + numbers[r_idx]
            if s == target:
                return [l_idx+1, r_idx+1]
            if s > target:
                r_idx -= 1
            else:
                l_idx += 1
        return [-1,-1]