class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        R, C = len(matrix), len(matrix[0])
        small = 100*1000
        if R ==1:
            return min(matrix[0])

        for i in range(1, R):
            for j in range(C):
                if C==1:
                    matrix[i][j] += matrix[i-1][j]
                elif C==2:
                    if j == 0:
                        matrix[i][j] += min(matrix[i-1][j], matrix[i-1][j+1])
                    else:
                        matrix[i][j] += min(matrix[i-1][j], matrix[i-1][j-1])
                else:
                    if j == 0:
                        matrix[i][j] += min(matrix[i-1][j], matrix[i-1][j+1])
                    elif j == C-1:
                        matrix[i][j] += min(matrix[i-1][j], matrix[i-1][j-1])
                    else:
                        matrix[i][j] += min(
                            matrix[i-1][j], matrix[i-1][j-1], matrix[i-1][j+1])
                if i == R-1 and small>matrix[i][j]:
                        small = matrix[i][j]
        # print(matrix)
        return small

