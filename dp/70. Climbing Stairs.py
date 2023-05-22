class Solution:
    def climbStairs(self, n: int) -> int:
        prev1 = 1
        prev2 = 0
        for i in range(1, n+1):
            prev1, prev2 = prev1+prev2, prev1
        return prev1