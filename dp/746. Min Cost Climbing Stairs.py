class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        ls = [0]*(len(cost)+1)

        for i in range(2, len(cost)+1):
            ls[i] = min(ls[i-1]+cost[i-1], ls[i-2]+cost[i-2])
        return ls[-1]