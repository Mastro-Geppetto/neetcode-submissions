class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix)
        n=len(matrix[0])
        #print(f"m x n = {m} x {n}")
        # print spiral index
        dirct = 1 # 1:E, 2:S, 3:W, 4:N
        total_steps = m*n
        result = []
        # m & n will start as right limit of index
        # 0 will start as left limit of index
        (row_start, row_end) = (0,m-1)
        (col_start, col_end) = (0,n-1)
        while total_steps:
            if dirct == 1: # east
                #print(f"➡️row:{str((row_start,row_end))}, col:{str((col_start,col_end))}", end=" ")
                cur_res = [matrix[row_start][i] for i in range(col_start,col_end+1,1)]
                row_start += 1
                total_steps -= len(cur_res)
                #print(f"curr:{str(cur_res)}")
                result += cur_res
                dirct = 2
            elif dirct == 2: # south
                #print(f"⬇️row:{str((row_start,row_end))}, col:{str((col_start,col_end))}", end=" ")
                cur_res = [matrix[i][col_end] for i in range(row_start,row_end+1,1)]
                col_end -= 1
                total_steps -= len(cur_res)
                #print(f"curr:{str(cur_res)}")
                result += cur_res
                dirct = 3
            elif dirct == 3: # west
                #print(f"⬅️row:{str((row_start,row_end))}, col:{str((col_start,col_end))}", end=" ")
                cur_res = [matrix[row_end][i] for i in range(col_end,col_start-1,-1)]
                row_end -= 1
                total_steps -= len(cur_res)
                #print(f"curr:{str(cur_res)}")
                result += cur_res
                dirct = 4
            elif dirct == 4: # north
                #print(f"⬆️row:{str((row_start,row_end))}, col:{str((col_start,col_end))}", end=" ")
                cur_res = [matrix[i][col_start] for i in range(row_end,row_start-1,-1)]
                col_start +=1
                total_steps -= len(cur_res)
                #print(f"curr:{str(cur_res)}")
                result += cur_res
                dirct = 1
        return result