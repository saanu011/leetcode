class Solution:
    def longestPalindrome(self, s: str) -> str:

        def check(i,j):
            l = j-i+1
            mid = i+(l//2)
            if l%2 == 0:
                a = s[mid:j+1]
                # print(s[i:mid], a)
                if s[i:mid] == a[::-1]:
                    # print(s[i:j])
                    return True
                return False
            else:
                a = s[mid+1:j+1]
                # print(s[i:mid], a)
                if s[i:mid] == a[::-1]:
                    return True
                return False
        L = len(s)
        if L == 1:
            return s
        dp = [[False]*L for _ in range(L)]
        # print(dp)
        res = [0, 0]
        for i in range(L):
            # print(i)
            dp[i][i] = True
        # print(dp)
        big = 0
        for i in range(L-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                big = 2
                res[0], res[1] = i, i+1

        # print(dp)
        for i in range(2, L):
            for k in range(0,L-i):
                # if i==2:
                #     print(k, s[i], s[k])
                # print(i,k)
                j = i+k
                if s[j] == s[k] and dp[k+1][j-1]:
                    dp[k][j] = True
                    # print(i,k)
                    res= [k, j]
        # print(dp)
        return s[res[0]:res[1]+1]
