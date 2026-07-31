class Union_find:
    def __init__(self,height,width) -> None:
        self.parent = []
        for x in range(height):
            self.parent.append([[x,y] for y in range(width)])
        self.size = [[1]*width for _ in range(height)]
        #print(self.parent)
        #print(self.size)
    def find_set(self, x,y ):
        # find parent
        if self.parent[x][y] == [x,y]:
            return [x,y]
        #print(f"find:{x}:{y}", self.parent[x][y])
        self.parent[x][y] = self.find_set( *self.parent[x][y] )
        return self.parent[x][y]
    def union_set(self, x_a,y_a, x_b,y_b ):
        a = self.find_set(x_a, y_a)
        b = self.find_set(x_b, y_b)
        if a == b:
            #print(f"\ta==b :: {a} and {b}")
            return
        print(f"union:({x_a},{y_a}) ({x_b},{y_b}) :: {a} and {b}", end=" ")
        if self.size[a[0]][a[1]] < self.size[b[0]][b[1]]:
            _ = a
            a = b
            b = _
        self.parent[b[0]][b[1]] = a
        self.size[a[0]][a[1]] += self.size[b[0]][b[1]]

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        union = Union_find(len(grid), len(grid[0]))
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1':
                    # add '1' neighbours
                    if x-1>=0 and grid[x-1][y] == '1':
                        union.union_set(x,y, x-1,y)
                    if y+1<len(grid[0]) and grid[x][y+1] == '1':
                        union.union_set(x,y, x,y+1)
                    if x+1<len(grid) and grid[x+1][y] == '1':
                        union.union_set(x,y, x+1,y)
                    if y-1>=0 and grid[x][y-1] == '1':
                        union.union_set(x,y, x,y-1)
        # find number of islands
        counter = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1' and union.parent[x][y] == [x,y]:
                    counter += 1
        return counter