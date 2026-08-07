class Solution:
    def find_point_of_rotation(self, nums):
        # ascending order
        if len(nums) == 1:
            return 0
        if nums[-1] > nums[0]:
            return len(nums)
        (l,r) = (0, len(nums)-1)
        m = 0
        while l<r:
            m = l+(r-l)//2
            #print(f"l:{l},m:{m},r:{m}")
            if nums[m] > nums[l]:
                # go right
                l = m
            else:
                # go left
                r = m
        print(f"l:{l},m:{m},r:{m}")
        return m

    def search(self, nums: List[int], target: int) -> int:
        # 1. find the point to rotation
        point = self.find_point_of_rotation(nums)
        # 2. now binary search in 2 sorted array
        l_a = nums[:point+1]
        l_b = nums[point+1:]
        print(f"a:{l_a}, b:{l_b}")
        import bisect
        index_1 = bisect.bisect_left(l_a, target)
        if index_1 < len(l_a) and l_a[index_1] == target:
            return index_1
        index_2 = bisect.bisect_left(l_b, target)
        if index_2 < len(l_b) and l_b[index_2] == target:
            return point+index_2+1
        return -1