class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if r*c != m*n:
            return mat
        oned = [item for sublist in mat for item in sublist]
        new = [[] for _ in range(r)]

        l = 0
        h = c
        for sublist in new: 
            sublist.extend(oned[l:h])
            l = h
            h = l + c
        return new   