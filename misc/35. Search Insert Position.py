class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = len(nums)

        def binary(left, right):
            if left > l-1:
                return l
            elif right < 0:
                return 0
            if left>right:
                if nums[left]<target:
                    return left+1
                elif nums[left]>target>nums[right]:
                    return left
                else:
                    return right
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            if nums[mid]>target:
                return binary(left, mid-1)
            else:
                return binary(mid+1, right)
        return binary(0, l-1)
                    