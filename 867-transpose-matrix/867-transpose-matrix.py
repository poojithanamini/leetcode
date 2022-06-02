class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []
        for i in range(len(matrix[0])):
            a=[]
            for j in range(len(matrix)):
                # print(matrix[j][i])
                a.append(matrix[j][i])
            res.append(a)
        return res