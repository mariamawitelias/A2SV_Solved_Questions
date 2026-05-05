class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        q = deque()
        q.append([1, 0])
        visit = set()
        board.reverse()
        def cord(square):
            r = (square - 1) // n
            c = (square - 1) % n
            if r%2:
                c = n - 1 - c
            return [r, c] 
        while q:
            node, moves = q.popleft()
            for i in range(1, 7):
                new = node + i
                r, c = cord(new)
                if board[r][c] != -1:
                    new = board[r][c]
                if new == n * n:
                    return moves + 1
                if new not in visit:
                    visit.add(new)
                    q.append([new, moves+1])
        return -1
                

                
            
                