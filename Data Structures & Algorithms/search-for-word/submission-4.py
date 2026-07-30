class Solution:
    def dfs(self,
            board, x, y,
            visited,
            word, idx):
        # 
        if idx >= len(word):
            return True
        if (x < 0 or x >= len(board)) or \
           (y < 0 or y >= len(board[0])):
            return False
        if (board[x][y] != word[idx]):
            return False
        #print(f"word[{idx}]:{word[idx]} board[{x}][{y}]:{board[x][y]} visited[{x}][{y}]:{visited[x][y]}")
        if visited[x][y]:
            return False
        # found match!
        # now we go down
        visited[x][y] = True
        res = (
            self.dfs(board, x-1,y, visited, word, idx+1) or
            self.dfs(board, x,  y+1, visited, word, idx+1) or
            self.dfs(board, x+1,y, visited, word, idx+1) or
            self.dfs(board, x,  y-1, visited, word, idx+1) 
            )
        visited[x][y] = False
        return res

    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False]*len(board[0])for _ in range(len(board))]
        for x in range(len(board)):
            for y in range(len(board[0])):
                if self.dfs(board, x,y, visited, word, 0):
                    return True
        return False
