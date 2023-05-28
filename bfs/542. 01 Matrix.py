# link: https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        queue = []
        R = len(mat)
        C = len(mat[0])

        for i in range(R):
            for j in range(C):
                if mat[i][j] == 0:
                    queue.append((i,j))
                else:
                    mat[i][j] = "*"
        for r, c in queue:
            for dr, dc in directions:
                row = r+dr
                col = c+dc
                if 0<=row<R and 0<=col<C and mat[row][col] == "*":
                    mat[row][col] = mat[r][c] + 1
                    queue.append((row, col))
        return mat
