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


# BFS
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        from collections import deque

        q = deque([s])
        visited = set()

        while q:
            s = q.popleft()
            for word in wordDict:
                if s.startswith(word):
                    new_s = s[len(word):]
                    if new_s == "":
                        return True
                    if new_s not in visited:
                        visited.add(new_s)
                        q.append(new_s)
        return False

