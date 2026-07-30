class Solution:
    def print_mat(self, matrix: List[List[int]]) -> None:
        print('-'*20)
        n = len(matrix)
        for rIdx in range(n):
            for cIdx in range(n):
                print(matrix[rIdx][cIdx], end="\t,")
            print()
        print('#'*20)
    
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        #self.print_mat(matrix)
        # 1. reflect by right diagonal
        for rIdx in range(n-1):
            for cIdx in range(n-rIdx-1):
                t_cIdx = n-rIdx-1
                t_rIdx = n-cIdx-1
                #print((rIdx,cIdx), "-", (t_rIdx,t_cIdx), end=" ")
                # swap
                t = matrix[rIdx][cIdx]
                #print(t, 'with', matrix[t_rIdx][t_cIdx])
                matrix[rIdx][cIdx] = matrix[t_rIdx][t_cIdx]
                matrix[t_rIdx][t_cIdx] = t
        #self.print_mat(matrix)

        # 2. reflect by  mid
        for rIdx in range((n+1)//2):
            t_rIdx = n-rIdx-1
            t = matrix[rIdx]
            matrix[rIdx] = matrix[t_rIdx]
            matrix[t_rIdx] = t
        #self.print_mat(matrix)