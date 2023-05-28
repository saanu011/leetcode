class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l = len(numbers)
        res = []
        flag = 0
        i ,j =0, l-1
        while i<l and j<l:
            if i >= j:
                j += 1
            else:
                if numbers[i]+numbers[j] == target:
                    return [i+1, j+1]
                if numbers[i]+numbers[j] < target:
                    i +=1
                else:
                    j-=1

        return res
                
