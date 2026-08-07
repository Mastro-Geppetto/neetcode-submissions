class Solution:
    def findMin(self, nums: List[int]) -> int:
        # we know its ascending order
        #   => right > left
        # so binary search is possible
        # we know its rotated
        # case 0 : edge cases
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return min(nums[0], nums[1])
        # case 1
        # NOT rotated IFF nums[-1] > nums[0]
        if nums[-1] > nums[0]:
            return nums[0]
        # cases other
        (left,right)=(0,len(nums)-1)
        mid = len(nums)//2
        while left < right:
            mid = left+(right-left)//2
            print(f"l:{left}:{nums[left]},m:{mid}:{nums[mid]},r:{right}:{nums[right]}")
            # skip sorted part
            if nums[mid] > nums[left]: # go right
                left = mid
                print('go right')
            else:
                right = mid
                print('go left')
        print(f"l:{left}:{nums[left]},m:{mid}:{nums[mid]},r:{right}:{nums[right]}")
        return nums[mid+1]