class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        l = len(nums)
        if l<=(2*k):
            return [-1 for _ in range(l)]

        res = []
        den = (2*k)+1

        currSum = 0
        for i in range(0, (2*k)):
            currSum += nums[i]

        for i in range(l):
            if i<k or i>l-k-1:
                res.append(-1)
            else:
                print(i)
                currSum += nums[i+k]
                res.append(currSum//den)
                currSum -= nums[i-k]
        return res


