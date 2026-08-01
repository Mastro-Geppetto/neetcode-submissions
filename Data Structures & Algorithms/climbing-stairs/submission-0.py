class Solution:
    def climbStairs(self, n: int) -> int:
        #climb[2] = 2
        # 1 step - 1 way [1]
        # 2 step - 2 way [all 1] [2]
        # 3 step - 3 way [all 1] [1,2]x2
        # 4 step - 5 way
        #   [all 1] [1,1,2]x3 [2,2]
        # 5 step - 8 way
        # [all 1], [2,1,1,1]x4, [2,2,1]xC(3,2)
        # 6 step - 13 way
        # [all 1], [2,1,1,1,1]x5, [2,2,1,1]xC(4,2), [2,2,2]
        # 7 step - 21
        # [all 1], [2,5x1]xC(6,1), [2x2,4x1]xC(5,2), [2x3,1]xC(4,3)
        # 8 step - 
        # C(8,0), C(7,1), C(6,2), C(5,3), C(4,4)
        steps = 0
        j=0
        for i in range(n,-1,-1):
            if j*2 <= n:
                #print(f"C({i},{j}) = {math.comb(i,j)}")
                steps += math.comb(i,j)
            j += 1
        return steps
