class Solution:
    def maxArea(self, heights: List[int]) -> int:
        (l_height, r_height) = (0,0)
        max_vol = 0
        (l_idx,r_idx) = (0,len(heights)-1)
        # edge case
        if r_idx == 1:
            return 1*min(heights[0], heights[1])
        # calculate volume at every step
        while l_idx < r_idx:
            # current volume = distance x min height
            c_vol = (r_idx-l_idx)*min(heights[l_idx], heights[r_idx])
            # max seen till now
            max_vol = max(max_vol, c_vol)
            # move smaller bar's pointer
            if heights[l_idx] >= heights[r_idx]:
                r_idx -= 1
            else:
                l_idx += 1
        return max_vol