class Solution:

    def isSafe(self, board, row, col, n):
        # Horizontally
        # for j in range(n):
        #     if board[row][j] == "Q":
        #         return False
        
        # Vertically
        for i in range(n):
            if board[i][col] == "Q":
                return False
        
        # Left Diagonal
        for lr, lc in zip(range(row, -1, -1), range(col, -1 ,-1)):
            if board[lr][lc] == 'Q':
                return False
        
        # Right Diagonal
        for rr, rc in zip(range(row, -1, -1), range(col, n)):
            if board[rr][rc] == "Q":
                return False
        
        return True

    
    def nQueeu(self:"Solution", board:list[list[str]], row:int, n:int, ans:list):
        if row == n:
             current_solution = ["".join(r) for r in board]
             ans.append(current_solution)
             return
            
        for col in range(n):
            if self.isSafe(board, row, col, n):
                board[row][col] = "Q"
                self.nQueeu(board, row+1, n, ans)
                board[row][col] = "."
                

    def solveNQueens(self, n: int) -> list[list[str]]:
        board = [["."] * n for _ in range(n)]
        ans = []
        # print(board)
        self.nQueeu(board, 0, n, ans)
        print(ans)
        return ans


n = 4
obj = Solution()
obj.solveNQueens(n)