class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return nums[0]
        ls = [0]*(l)
        ls[0], ls[1] = nums[0], nums[1]

        for i in range(2, l):
            if i>2:
                ls[i] = nums[i] + max(ls[i-2], ls[i-3])
            else:
                ls[i] = nums[i] + ls[i-2]
        return max(ls[-1], ls[-2])

