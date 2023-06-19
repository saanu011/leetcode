class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        point = 0

        for e in gain:
            point += e
            if point > ans:
                ans = point
        return ans


