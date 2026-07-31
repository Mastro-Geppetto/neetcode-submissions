class Solution:
    def dfs(self, grid, x,y):
        # we check for x,y range & value of cell == '0'
        if x < 0 or y < 0 or x >=len(grid) or y >= len(grid[0]):
            return
        if grid[x][y] == '0':
            return
        #print(f"dfs:{x}:{y}={grid[x][y]}")
        # increment & reset cell
        grid[x][y] = '0'
        # now, check neighbouring cells
        self.dfs(grid, x-1, y)
        self.dfs(grid, x  , y+1)
        self.dfs(grid, x+1, y)
        self.dfs(grid, x  , y-1)

    def numIslands(self, grid: List[List[str]]) -> int:
        # find first "1" and dfs
        count = 0
        # inc count when we see '1'
        # after arrival at '1' set it to '0' and dfs
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1':
                    count += 1
                    self.dfs(grid,x,y)
        return count