class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # fill a hash table
        table = {}
        # store value -vs- index
        for idx in range(len(nums)):
            table[nums[idx]] = idx
        print(table)
        # using table, search for idx
        for idx in range(len(nums)):
            c_num = nums[idx]
            t_num = target - c_num
            if t_num in table:
                o_idx = table[t_num]
                if o_idx != idx:
                    result = [idx, o_idx]
                    return sorted(result)
        # else error
        return [0,0]