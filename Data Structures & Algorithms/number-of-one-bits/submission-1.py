class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0:
            return 0
        one_count = 0
        while n:
            if 1 & n:
                one_count += 1
            n = n>>1
        return one_count
            