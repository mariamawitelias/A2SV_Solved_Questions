class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def inbound(r, c):
            return 0 <= r < len(board) and 0 <= c < len(board[0])
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def dfs(r, c):
            if not inbound(r, c):
                return
            if board[r][c] != "O":
                return
            board[r][c] = "T"
            for ro, col in direction:
                newr = ro + r
                newc = col + c
                dfs(newr, newc)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O" and (r in [0, len(board)-1] or c in [0, len(board[0])-1]):
                    dfs(r, c)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O':
                    board[r][c] = "X"
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "T":
                    board[r][c] = "O"
        
        
                
