class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        def partition(low, high):
            i = low-1
            p = nums[high]
            for j in range(low, high):
                if nums[j] <= p:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[i+1], nums[high] = nums[high], nums[i+1]
            return i+1

        def sort(low, high):
            if low<high:
                part = partition(low, high)
                sort(low, part-1)
                sort(part+1, high)

        sort(0, len(nums)-1)
        self.nums = nums
        self.k = k
        # print(nums)

    def add(self, val: int) -> int:
        l = len(self.nums)
        if l == 0:
            self.nums = [val]

        for i in range(l-1, -1, -1):
            if val >= self.nums[i]:
                self.nums = self.nums[:i+1] + [val] + self.nums[i+1:]
                break
            if i == 0:
                self.nums = [val] + self.nums

        l = len(self.nums)

        return self.nums[l-self.k]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)