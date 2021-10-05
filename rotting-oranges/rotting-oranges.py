class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])

        fresh = 0
        queue = []
        visited = set()

        for i in range(0, r):
            for j in range(0, c):
                if grid[i][j]==2:
                    queue.append((i,j, 0))
                    visited.add((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        if not fresh:
            return 0

        def bfs(fresh):
            while queue:
                size = len(queue)

                while size:
                    x, y, time = queue.pop(0)

                    if x<r-1 and (x+1, y) not in visited and grid[x+1][y]==1:
                        queue.append((x+1, y, time+1))
                        visited.add((x+1, y))
                        fresh-=1

                    if x>0 and (x-1, y) not in visited and grid[x-1][y]==1:
                        queue.append((x-1, y, time+1))
                        visited.add((x-1, y))
                        fresh-=1

                    if y<c-1 and (x, y+1) not in visited and grid[x][y+1]==1:
                        queue.append((x, y+1, time+1))
                        visited.add((x, y+1))
                        fresh-=1

                    if y>0 and (x, y-1) not in visited and grid[x][y-1]==1:
                        queue.append((x, y-1, time+1))
                        visited.add((x, y-1))
                        fresh-=1

                    size-=1

            return time if not fresh else -1

        return bfs(fresh)