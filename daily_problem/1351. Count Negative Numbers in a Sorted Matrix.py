class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        ans = 0
        k = C-1
        for i in range(R):
            while k>=0 and grid[i][k] <0:
                k -=1
            ans += C-k-1
        return ans

