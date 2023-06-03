# link: https://leetcode.com/problems/minimum-path-sum/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        for i in range(1,R):
            grid[i][0] += grid[i-1][0]
            
        for i in range(1,C):
            grid[0][i] += grid[0][i-1]

        for i in range(1,R):
            for j in range(1,C):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        # print(grid)
        return grid[R-1][C-1]
