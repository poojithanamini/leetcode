class Solution:
    def __init__(self):
        self.res=0
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def backtrack(x,y,remain):
            if grid[x][y]==2 and remain==1:
                self.res+=1
                return
            remain-=1
            temp=grid[x][y]
            grid[x][y]=-3
            travel=[(0,1),(1,0),(-1,0),(0,-1)]
            for dx,dy in travel:
                nx,ny=dx+x,dy+y
                if 0<=nx<row and 0<=ny<col and grid[nx][ny]>=0:
                    backtrack(nx,ny,remain)
            grid[x][y]=temp
        row,col,not_obstacle=len(grid),len(grid[0]),0
        for i in range(row):
            for j in range(col):
                if grid[i][j]>=0:
                    not_obstacle+=1
                if grid[i][j]==1:
                    start_row,start_col=i,j
        backtrack(start_row,start_col,not_obstacle)
        return self.res