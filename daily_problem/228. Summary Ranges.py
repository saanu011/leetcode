class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        ls = []
        start= nums[0]
        end= nums[0]-1
        for i in range(1, len(nums)):
            if nums[i]-nums[i-1] == 1:
                end = nums[i]
            else:
                if end<start:
                    ls.append(str(start))
                    start = nums[i]
                else:
                    ls.append(str(start)+"->"+str(end))
                    start = nums[i]
        if end<start:
            ls.append(str(start))
        else:
            ls.append(str(start)+"->"+str(end))
        return ls
                
