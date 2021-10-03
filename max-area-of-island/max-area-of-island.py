class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        
        self.row_dim = len(grid)
        self.col_dim = len(grid[0])

        biggest = 0
        for i in range(self.row_dim ):
            for j in range(self.col_dim):
                if grid[i][j] == 1:
                    biggest = max([biggest, self.mark_and_get_size(i, j)])
                    
        return biggest
    
    def mark_and_get_size(self, i, j):
        """calculate total size of island that touches (i, j)"""
        if not ((0 <= i < self.row_dim) and (0 <= j < self.col_dim)):
			# out of bounds
            return 0
        if self.grid[i][j] != 1:
			# not an island or have counted it already 
            return 0
        else:
			# this is part of an island.
            # we dont want to double count this square 
            # mark it as 0, count it as 1, and look left, down, right, up
            self.grid[i][j] = 0
            l = self.mark_and_get_size(i - 1, j)
            d = self.mark_and_get_size(i, j - 1)
            r = self.mark_and_get_size(i + 1, j)
            u = self.mark_and_get_size(i, j + 1)
            return 1 + l + d + r + u