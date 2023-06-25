# https://leetcode.com/problems/number-of-islands


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        visited = set()
        R, C = len(grid), len(grid[0])
        res = 0

        for i in range(R):
            for j in range(C):
                if grid[i][j] == "1" and (i,j) not in visited:
                    def dfs(r,c):
                        if grid[r][c] == "1" and (r,c) not in visited:
                            visited.add((r,c))
                            if r>=1:
                                dfs(r-1,c)
                            if r+1<R:
                                dfs(r+1,c)
                            if c>=1:
                                dfs(r,c-1)
                            if c+1<C:
                                dfs(r,c+1)
                    

                    visited.add((i,j))
                    res += 1
                    if i>=1:
                        dfs(i-1,j)
                    if i+1<R:
                        dfs(i+1,j)
                    if j>=1:
                        dfs(i,j-1)
                    if j+1<C:
                        dfs(i,j+1)

        return res


