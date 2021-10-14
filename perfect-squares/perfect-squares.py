class Solution:
    def numSquares(self, n: int) -> int:
        if n == 1: return 1
        squares = [i*i for i in range(1,n) if i*i <= n]    
        queue = deque([(n,0)]) 

        while queue:
            num,count = queue.popleft()
            count += 1    

            for square in reversed(squares): 
                if num - square == 0:   
                    return count
                else:
                    queue.append((num - square, count)) 