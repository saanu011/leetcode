# link: https://leetcode.com/problems/longest-arithmetic-subsequence/
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 2:
            return l
        # store length of every difference
        dp = [{} for _ in range(l)]
        big = 2

        for i in range(l):
            for j in range(i):
                diff = nums[i]-nums[j]
                if diff in dp[j]:
                    dp[i][diff] = dp[j][diff]+1
                else:
                    dp[i][diff] = 2
                big = max(dp[i][diff], big)
        return big
        

        


        

