# link: https://leetcode.com/problems/shortest-path-in-binary-matrix/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        R, C = len(grid), len(grid[0])
        if grid[0][0] != 0:
            return -1
        if grid[R-1][C-1] != 0:
            return -1

        directions = [[-1,-1],[-1,0],[-1,1],
                        [0,-1],[0,1],
                        [1,-1],[1,0],[1,1]]
        queue = []
        
        for i in range(R):
            for j in range(C):
                if i == 0 and j == 0:
                    queue.append((i,j))
                elif grid[i][j] == 0:
                    grid[i][j] = '*'
                elif grid[i][j] == 1:
                    grid[i][j] = '#'
        
        for r, c in queue:
            for dr, dc in directions:
                row = r+dr
                col = c+dc
                if 0<=row<R and 0<=col<C and grid[row][col] == '*':
                    # print("inside", row, col, r, c)
                    a = grid[r][c] + 1
                    if type(grid[row][col]) == int:
                        if grid[row][col]>a:
                            grid[row][col] = a
                            queue.append((row, col))
                    else:
                        grid[row][col] = a
                        queue.append((row, col))

        # print(grid)
        return grid[R-1][C-1]+1 if type(grid[R-1][C-1]) == int else -1
        
