class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        board.reverse()
        def getCoordinates(space):
            space -= 1
            r = space // n
            c = space % n
            if r % 2:
                c = n - 1 - c
            return [r, c]
            
        visited = set()
        q = deque([(1, 0)])
        while q:
            cur, depth = q.popleft()

            for i in range(1, 7):
                nextSquare = cur + i

                r, c = getCoordinates(nextSquare)
                if board[r][c] != -1:
                    nextSquare = board[r][c]

                if nextSquare == n**2: return depth + 1
                
                if nextSquare not in visited:
                    visited.add(nextSquare)
                    q.append((nextSquare, depth + 1))

        return -1