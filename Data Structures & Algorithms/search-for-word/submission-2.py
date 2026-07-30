class Solution:
    def next_positions(self,
                        max_row,max_col,
                        curr_x, curr_y,
                        prev_positions):
        positions = set()
        positions.add( (curr_x-1, curr_y) ) # North
        positions.add( (curr_x+1, curr_y) ) # South
        positions.add( (curr_x,   curr_y+1) ) # East
        positions.add( (curr_x,   curr_y-1) ) # West
        # remove prev_positions
        next_positions = positions.difference(prev_positions)
        #print("\tnext_positions:", next_positions)
        return next_positions
    
    def bfs(self,
            board, x, y, prev_positions,
            word, idx):
        if idx >= len(word):
            return True
        (max_row,max_col) = (len(board), len(board[0]))
        # assuming x,y matches word[idx-1]
        # create a local copy
        new_prev_positions = prev_positions.copy()
        new_prev_positions.append( ( x, y) )
        #
        next_positions = self.next_positions(
                            max_row,max_col,
                            x,y,
                            set(new_prev_positions) )
        for (next_x, next_y) in next_positions:
            if board[next_x][next_y] == word[idx]:
                #print("bfs:", f"board[{next_x}][{next_y}]==word[{idx}]")
                if self.bfs(
                    board, next_x, next_y, new_prev_positions,
                    word, idx+1):
                    return True
            #else:
            #    print(f'bfs: board[{next_x}][{next_y}] ≠ word[{idx}]')
        new_prev_positions.remove( ( x, y) )
        #print(f'bfs:failed board[{x}][{y}]')
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        prev_positions = []
        # adding a boundary
        # rows
        for x in range(-1,len(board)+1):
            prev_positions.append( (x,-1) )
            prev_positions.append( (x,len(board[0])) )
        # cols
        for y in range(-1,len(board[0])+1):
            prev_positions.append( (-1,y) )
            prev_positions.append( (len(board),y) )
        ## Search for first char
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == word[0]:
                    #print("bfs:", f"board[{x}][{y}]==word[0]")
                    if self.bfs(board, x,y, prev_positions,
                                word, 1): # idx=1 as 0 already matched
                        return True
                    #print(f"board[{x}][{y}] didn't work!!")
        return False
        