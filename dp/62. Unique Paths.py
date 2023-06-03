#  link: https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n==1:
            return 1

        grid = [[0]*n]*m
        grid[0] = [1]*n
        grid[0][0] = [0]
        for i in range(1, m):
            grid[i][0] = 1
        # print(grid)
        directions = [[0,1], [1,0]]

        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] = grid[i-1][j]+grid[i][j-1]


        return grid[m-1][n-1]
        