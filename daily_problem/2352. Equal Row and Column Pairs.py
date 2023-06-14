class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        c = 0
        temp = []
        for i in range(len(grid)):
            t1 = []
            for j in range(len(grid[0])):
                t1.append(grid[j][i])
            temp.append(t1)

        for i in range(len(grid)):
            for j in range(len(temp)):
                if grid[i] == temp[j]:
                    c+=1
        return c
                