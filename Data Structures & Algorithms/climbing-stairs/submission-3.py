class Solution:
    def __init__(self) -> None:
        self.steps = []

    def bfs(self,i,n ):
        if i>n:
            return 0
        if i==n:
            return 1
        # check if we have already computed ?
        if self.steps[i] != -1:
            return self.steps[i]
        # else calculate
        self.steps[i] = self.bfs(i+1, n)+self.bfs(i+2, n)
        return self.steps[i]

    def climbStairs(self, n: int) -> int:
        '''
        DP top down(Memoization):
        1. Recursive path count Solution
            we start from i=0 (top)
            we take either 1 or 2 steps
            total num of steps = 1 step + 2 step path count
                if i == n(at bottom),
                    return 1
                if i > n (out of bound)
                    return 0
                current steps = bfs(i+1) + bfs(i+2)
        2. Memoization : we use a array to skip recalculations
            steps = [-1]*(n+1)
            steps[n] = 1
            if i == n(at bottom)
                return 1
            if i > n (out of bound)
                return 0
            current steps = (bfs(i+1) if steps[i+1]!=-1 else steps[i+1]) + (bfs(i+2) if if steps[i+2]!=-1 else steps[i+2])
        '''
        self.steps = [-1]*(n+1)
        return self.bfs(0,n)
        return steps[0]