# link: https://leetcode.com/problems/word-break

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        dp = [False]*(n+1)

        dp[0] = True

        for i in range(n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    print(s[j:i])
                    print(dp)
                    dp[i] = True
                    break
        return dp[n]

