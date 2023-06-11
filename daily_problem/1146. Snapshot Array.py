#  link: https://leetcode.com/problems/snapshot-array/

class SnapshotArray:

    def __init__(self, length: int):
        self.list = [[(0,0)] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        arr = self.list[index]
        if arr[-1][0] == self.snap_id:
            arr.pop()
        arr.append((self.snap_id, val))
        self.list[index] = arr

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id-1

    def get(self, index: int, snap_id: int) -> int:
        ls = self.list[index]
        def binary(low, high):
            if low>high:
                if snap_id < ls[high][0]:
                    return ls[high-1][1]
                elif snap_id > ls[high][0] and (high == len(ls)-1 or snap_id < ls[low][0]):
                    return ls[high][1]
                else:
                    return ls[low][1]
            mid = (low+high)//2
            if ls[mid][0] == snap_id:
                return ls[mid][1]
            if ls[mid][0] > snap_id:
                return binary(low, mid-1)
            else:
                return binary(mid+1, high)

        return binary(0, len(ls)-1)
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)