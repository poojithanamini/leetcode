class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        height = len(image)
        width = len(image[0])
        startingColor = image[sr][sc]
        
        def dfs(r,c):
            if (0 <= r < height and 0 <= c < width and image[r][c] == startingColor):
                image[r][c] = -1
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)
        
        
        dfs(sr, sc)
        
        for i in range(len(image)):
            for j in range(len(image[0])):
                if (image[i][j] == -1):
                    image[i][j] = newColor
        
        return image