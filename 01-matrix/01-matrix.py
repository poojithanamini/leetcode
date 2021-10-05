class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        queue=[]
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    queue.append((i,j))
                else:
                    mat[i][j]='#'
        for r,c in queue:
            for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
                nr=r+dx
                nc=c+dy
                if 0<=nr<m and 0<=nc<n and mat[nr][nc]=='#':
                    mat[nr][nc]=mat[r][c]+1
                    queue.append((nr,nc))
        return mat