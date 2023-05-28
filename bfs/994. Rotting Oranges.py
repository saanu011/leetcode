#  link: https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions =[[1,0], [-1,0], [0,1], [0,-1]]
        R = len(grid)
        C = len(grid[0])
        big = 0
        queue = []

        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    grid[i][j] = "*"
                elif grid[i][j] == 2:
                    grid[i][j] = 0
                    queue.append((i,j))
                elif grid[i][j] == 0:
                    grid[i][j] = "#"
        
        # print(grid)
        for r, c in queue:
            for dr, dc in directions:
                row = r+dr
                col = c+dc
                # print(row, col)
                if 0<=row<R and 0<=col<C and grid[row][col] == "*":
                    grid[row][col] = grid[r][c]+1
                    queue.append((row, col))
                    if big<grid[row][col]:
                        big = grid[row][col]
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] == "*":
                    return -1
        return big

        
        