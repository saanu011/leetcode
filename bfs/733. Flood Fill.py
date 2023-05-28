class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        queue = [(sr,sc)]
        # visited = set()
        # visited.add((sr,sc))
        oldColor = image[sr][sc]
        image[sr][sc] = color

        for r, c in queue:
            for dr, dc in directions:
                row = r+dr
                col = c+dc
                if 0<=row<len(image) and 0<=col<len(image[0]) and image[row][col] == oldColor:
                    image[row][col] = color
                    # if visited
                    queue.append((row, col))
                    print(row, col, queue)
        return image
