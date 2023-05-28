class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        queue = []
        R, C = len(grid), len(grid[0])
        visited = set()
        ls = [0, 0]

        big = 0
        def move(r, c):
            if grid[r][c] == 1 and (r,c) not in visited:
                visited.add((r,c))
                ls[1] += 1
                if r-1>=0:
                    move(r-1, c)
                if r+1<R:
                    move(r+1, c)
                if c-1>=0:
                    move(r, c-1)
                if c+1<C:
                    move(r, c+1)

        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1 and (i,j) not in visited:
                    move(i,j)
                    if ls[0]<ls[1]:
                        ls[0] = ls[1]
                    ls[1] = 0
        return ls[0]
