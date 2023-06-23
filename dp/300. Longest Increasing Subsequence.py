# link: https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # save last element of subsequenece and length
        dp = [(nums[0], 1)]
        l = len(nums)

        big = 1
        for i in range(1, l):
            dp.append((nums[i], 1))
            for j in range(i):
                if nums[j] < nums[i] and dp[j][1] >= dp[i][1]:
                    dp[i] = (nums[i], dp[j][1]+1)
                if dp[i][1]>big:
                    big = dp[i][1]
        
        return big

