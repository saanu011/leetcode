# link: https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        R, C = len(obstacleGrid), len(obstacleGrid[0])
        if R == 1 and C==1:
            if obstacleGrid[0][0] == 1:
                return 0
            return 1

        for i in range(R):
            for j in range(C):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = '*'
        # print(obstacleGrid)
        
        for i in range(1, R):
            if obstacleGrid[i][0] != '*':
                if obstacleGrid[i-1][0] == '*':
                    obstacleGrid[i][0] = '*'
                else:
                    obstacleGrid[i][0] = 1
        # print(obstacleGrid)
        for i in range(1, C):
            if obstacleGrid[0][i] != '*':
                if obstacleGrid[0][i-1] == '*':
                    obstacleGrid[0][i] = '*'
                else:
                    obstacleGrid[0][i] = 1
        # print(obstacleGrid)
        
        for i in range(1,R):
            for j in range(1,C):
                if obstacleGrid[i][j] != '*':
                    if obstacleGrid[i][j-1] == '*' and obstacleGrid[i-1][j] == '*':
                        obstacleGrid[i][j] = '*'
                    elif obstacleGrid[i][j-1] == '*':
                        obstacleGrid[i][j] = obstacleGrid[i-1][j]
                    elif obstacleGrid[i-1][j] == '*':
                        obstacleGrid[i][j] = obstacleGrid[i][j-1]
                    else:
                        obstacleGrid[i][j]=obstacleGrid[i][j-1]+obstacleGrid[i-1][j]
        # print(obstacleGrid)
        if obstacleGrid[R-1][C-1] == '*':
            return 0
        return obstacleGrid[R-1][C-1]

