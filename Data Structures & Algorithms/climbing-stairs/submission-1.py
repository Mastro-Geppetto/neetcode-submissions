class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        # DP bottom up :
        we can either go -1 step or -2 to reach bottom
                _5: -1->[4]or -2->[3]   : 5 + 3
              _4 : -1->[3] or -2->[2]   : 3 + 2
            _3 reach -1->[2] or -2->[1] : 2 + 1
          _2 reach -1->[1] or -2->[0]   : 2
        _1 reach -1->[0]                : 1
        '''
        steps = [1]*(n+1)
        for i in range(2,n+1):
            #print(f"step[{i}] = -1:{steps[i-1]} + -2:{steps[i-2]}")
            steps[i] = steps[i-1] + steps[i-2]
        return steps[n]