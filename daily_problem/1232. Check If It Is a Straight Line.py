class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        l = len(coordinates)
        if l == 2:
            return True
        # y = mx +c
        c1, c2 = coordinates[0], coordinates[1]
        num = (c2[1]-c1[1])
        den = (c2[0]-c1[0])
        if den == 0 :
            for i in range(1, l):
                if coordinates[i][0] != (coordinates[0][0]):
                    return False
            return True

        m = num/den
        c = c2[1]-(c2[0]*m)

        #  y = m*x + c
        for i in range(2, l):
            if coordinates[i][1] != (m*coordinates[i][0])+c:
                return False
        return True

