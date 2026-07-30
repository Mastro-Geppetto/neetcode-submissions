class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows2set = set()
        cols2set = set()
        # find col & rows to set to zero
        for rIdx in range(len(matrix)):
            row = matrix[rIdx]
            for cIdx in range(len(row)):
                if row[cIdx] == 0:
                    cols2set.add(cIdx)
                    rows2set.add(rIdx)
        # now set to zero
        for rIdx in rows2set:
            matrix[rIdx] = [0] * len(matrix[rIdx])
        for cIdx in cols2set:
            for row in matrix:
                row[cIdx] = 0
        