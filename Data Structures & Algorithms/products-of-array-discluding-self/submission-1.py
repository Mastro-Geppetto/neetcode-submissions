class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        (mul_l, mul_r) = (nums.copy(),nums.copy())
        for i in range(1, len(mul_l)):
            mul_l[i] *= mul_l[i-1]
        for i in range(len(mul_r)-2, -1, -1):
            mul_r[i] *= mul_r[i+1]
        print(mul_l)
        print(mul_r)
        # magic !
        first_val = mul_r[1]
        for i in range(1, len(mul_r)-1):
            mul_r[i] = mul_l[i-1]*mul_r[i+1]
        # set the first & last one
        mul_r[0]=first_val
        mul_r[-1]=mul_l[-2]
        print(mul_r)
        return mul_r