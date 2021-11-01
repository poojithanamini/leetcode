class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        stack = set()
        
        for r in range(rows):
            for c in (0, cols - 1):
                if board[r][c] == 'O':
                    board[r][c] = 'C'
                    stack.add((r, c))
        
        for c in range(cols):
            for r in (0, rows - 1):
                if board[r][c] == 'O':
                    board[r][c] = 'C'
                    stack.add((r, c))
        
		# Iteratively go through all 4 neighboring cells of the cells in the stack
		# Change those holding 'O' to 'C' and add their positions to the stack
		# Since those already captured are marked as 'C', it ensures the check does not go backward
		
        drdc = ((0, 1), (1, 0), (0, -1), (-1, 0))
        while stack:
            r, c = stack.pop()
            for dr, dc in drdc:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'O':
                    board[nr][nc] = 'C'
                    stack.add((nr, nc))
        
		# Modify the orignal matrix so that only cells holding 'C' will be marked as 'O', while the rest being 'X'
		
        for r in range(rows):
            for c in range(cols):
                board[r][c] = 'O' if board[r][c] == 'C' else 'X'