# link: https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        big = 0
        R, C = len(matrix), len(matrix[0])
        for i in range(R):
            if matrix[i][0] == "1":
                matrix[i][0] = 1
                big = 1
            else:
                matrix[i][0] = 0
        # print(matrix)
        for i in range(1, C):
            if matrix[0][i] == "1":
                matrix[0][i] = 1
                big = 1
            else:
                matrix[0][i] = 0
        # print(matrix)
        for i in range(1, R):
            for j in range(1, C):
                if matrix[i][j] == "1":
                    matrix[i][j] = min(matrix[i-1][j], matrix[i-1][j-1], matrix[i][j-1])+1
                else:
                    matrix[i][j] = 0
                if matrix[i][j]>big:
                    big = matrix[i][j]
        # print(matrix)
        return big**2
