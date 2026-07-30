class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        (l_ptr, r_ptr, window_max_sum, max_sum) = (0, 1, 0, 0)
        # check rest of them!
        while r_ptr < len(prices):
            print("p_c", window_max_sum, 'l',l_ptr, 'r', r_ptr )
            if prices[r_ptr] > prices[l_ptr]:
                window_max_sum = prices[r_ptr]-prices[l_ptr]
                max_sum = max(max_sum, window_max_sum)
            else:
                window_max_sum = 0
                l_ptr = r_ptr
            r_ptr += 1
        return max_sum
