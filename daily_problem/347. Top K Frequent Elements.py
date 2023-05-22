class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        vector = []

        for e in nums:
            if e not in d:
                d[e] = 1
            else:
                d[e] += 1
        for key, val in d.items():
            vector.append((key,val))
        def partition(low, high):
            p = vector[high][1]
            i = low-1
            for j in range(low, high):
                if vector[j][1] <= p:
                    i += 1
                    vector[j], vector[i] = vector[i], vector[j]
            vector[high], vector[i+1] = vector[i+1], vector[high]
            return i+1
        def sortTupleList(low, high):
            if low<high:
                part = partition(low, high)
                # print(vector[low:part])
                sortTupleList(low, part-1)
                # print(vector[part:high])
                sortTupleList(part+1, high)
        sortTupleList(0, len(vector)-1)
        res = []
        while k>0:
            res.append(vector[len(vector)-k][0])
            k-=1
        return res
        






        
