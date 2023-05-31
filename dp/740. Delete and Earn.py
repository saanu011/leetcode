# link: https://leetcode.com/problems/delete-and-earn/

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        max_value = max(nums)

        max_1 = 0
        max_2 = 0

        ls = [0]*(max_value+1)
        dp = [0]*(max_value+1)

        for e in nums:
            ls[e] += e
            print("e", e, "ls[e]", ls[e])
        print("ls: ", ls)

        for e in ls:
            max_1, max_2 = max_2, max(e+max_1, max_2)
            # print("max_1: ", max_1, "max_2: ", max_2)
        return max_2
        
        # dp[0] = ls[0]
        # if len(dp) == 1:
        #     return dp[0]
        # dp[1] = ls[1]
        # for i in range(2, len(ls)):
        #     if i>2:
        #         dp[i] = max(ls[i-1]+ls[i-3], ls[i]+ls[i-2])
        #     else:
        #         dp[i] = max(ls[i-1], ls[i]+ls[i-2])
        # print(dp)
        # return max(dp[-1], dp[-2])



