class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        l = len(triangle)
        if l == 1:
            return triangle[0][0]
        
        
        ans = []
        ans.append([triangle[0][0]])
        small = 10000000
        for i in range(1, l):
            temp = []
            for j in range(i+1):
                if j == 0:
                    a = triangle[i][j] + ans[i-1][j]
                elif j == i:
                    a = triangle[i][j] + ans[i-1][j-1]
                else:
                    a = triangle[i][j] + min(ans[i-1][j], ans[i-1][j-1])
                if i == l-1 and small>a:
                    small =a

                # print("a", a)
                temp.append(a)
            # print("temp", temp)
            ans.append(temp)
        return small

        # second approach - incomplete
        ans = [0]*l
        ans[0] = triangle[0][0]
        j = 0
        for i in range(1, l):
            e = triangle[i]
            a = e[j]
            if e[j]>e[j+1]:
                j += 1
                a = e[j]
            ans[i] = ans[i-1] + a
        return ans[l-1]
