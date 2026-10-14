class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        s = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    s.add((i,j))
        
        for cord in s:
            i,j = cord
            for y in range(n):
                matrix[i][y] = 0
            for x in range(m):
                matrix[x][j] = 0