class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:

        def partition(low, high):
            p = arr[high]
            i = low-1

            for j in range(low, high):
                if arr[j]<=p:
                    i += 1
                    arr[j], arr[i] = arr[i], arr[j]
                # print(arr, i)
            # print(i)
            arr[high], arr[i+1] = arr[i+1], arr[high]
            return i+1

        def sort(low, high):
            if low<high:
                p = partition(low, high)
                sort(low, p-1)
                sort(p+1, high)
        
        sort(0,len(arr)-1)
        # print(arr)
        diff = arr[1]-arr[0]
        for i in range(2,len(arr)):
            if arr[i] - arr[i-1] !=diff:
                return False
        return True

