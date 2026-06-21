import string
import copy

class Solution:
    def isSafe(self, board, row, col, digit):
        # Horizontally
        for j in range(9):
            if board[row][j] == digit:
                return False

        # Vertically
        for i in range(9):
            if board[i][col] == digit:
                return False

        # 3x3 Grid
        startRow = (row // 3) * 3
        startCol = (col // 3) * 3

        for gr in range(startRow, startRow + 3):
            for gc in range(startCol, startCol + 3):
                if board[gr][gc] == digit:
                    return False

        return True

    def sudoku(self, board, row, col):
        # Base case: If we reach row 9, the board is successfully filled
        if row == 9:
            return True
        
        # Safely calculate the next cell coordinates
        nextRow = row + (col + 1) // 9
        nextCol = (col + 1) % 9
        
        # If the cell is already filled, move to the next one immediately
        if board[row][col] != '.':
            return self.sudoku(board, nextRow, nextCol)
    
        # Try placing digits 1-9
        for digit in string.digits[1:]:
            if self.isSafe(board, row, col, digit):
                board[row][col] = digit
                
                # If this path leads to a successful solution, stop and return True
                if self.sudoku(board, nextRow, nextCol):
                    return True
                
                # Backtrack if it didn't work out
                board[row][col] = '.'

        return False

    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        RED = '\033[91m'
        GREEN = '\033[92m'
        CYAN = '\033[36m'
        RESET = '\033[0m'
        
        print(f"{CYAN}====================={RESET}")
        for r in range(9):
            if r > 0 and r % 3 == 0:
                print(f"{CYAN}------+-------+------{RESET}")
                
            row_str = []
            for c in range(9):
                if c > 0 and c % 3 == 0:
                    row_str.append(f"{CYAN}|{RESET}")
                
                # If it was empty originally, highlight it in GREEN
                if board[r][c] == '.':
                    row_str.append(f"{RED}{board[r][c]}{RESET}")
                else:
                    row_str.append(board[r][c])
                    
            print(" ".join(row_str))
        print(f"{CYAN}====================={RESET}")

        original_board = copy.deepcopy(board)

        # SUDOKU SOLVER CALLED
        self.sudoku(board, 0, 0)

        print(f"{CYAN}====SUDOKU SOLVER===={RESET}")
        
        # 4. Beautifully print the grid with colors
        print(f"{CYAN}====================={RESET}")
        for r in range(9):
            if r > 0 and r % 3 == 0:
                print(f"{CYAN}------+-------+------{RESET}")
                
            row_str = []
            for c in range(9):
                if c > 0 and c % 3 == 0:
                    row_str.append(f"{CYAN}|{RESET}")
                
                # If it was empty originally, highlight it in GREEN
                if original_board[r][c] == '.':
                    row_str.append(f"{GREEN}{board[r][c]}{RESET}")
                else:
                    row_str.append(board[r][c])
                    
            print(" ".join(row_str))
        print(f"{CYAN}====================={RESET}")
        


class Solution2:
    def solveSudoku(self, board):
        RED = '\033[91m'
        GREEN = '\033[92m'
        CYAN = '\033[36m'
        RESET = '\033[0m'
        
        print(f"{CYAN}====================={RESET}")
        for r in range(9):
            if r > 0 and r % 3 == 0:
                print(f"{CYAN}------+-------+------{RESET}")
                
            row_str = []
            for c in range(9):
                if c > 0 and c % 3 == 0:
                    row_str.append(f"{CYAN}|{RESET}")
                
                # If it was empty originally, highlight it in GREEN
                if board[r][c] == '.':
                    row_str.append(f"{RED}{board[r][c]}{RESET}")
                else:
                    row_str.append(board[r][c])
                    
            print(" ".join(row_str))
        print(f"{CYAN}====================={RESET}")

        original_board = copy.deepcopy(board)
        
        # Logic
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        # Preprocess board
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    empty.append((i, j))
                else:
                    num = board[i][j]
                    rows[i].add(num)
                    cols[j].add(num)
                    box = (i // 3) * 3 + (j // 3)
                    boxes[box].add(num)

        def backtrack(index):
            # solved
            if index == len(empty):
                return True

            row, col = empty[index]
            box = (row // 3) * 3 + (col // 3)

            for digit in "123456789":
                
                # O(1) checking
                if digit in rows[row]:
                    continue
                if digit in cols[col]:
                    continue
                if digit in boxes[box]:
                    continue

                # place
                board[row][col] = digit
                rows[row].add(digit)
                cols[col].add(digit)
                boxes[box].add(digit)

                if backtrack(index + 1):
                    return True

                # undo
                board[row][col] = "."
                rows[row].remove(digit)
                cols[col].remove(digit)
                boxes[box].remove(digit)

            return False

        backtrack(0)
    

        # SUDOKU SOLVER CALLED

        print(f"{CYAN}====SUDOKU SOLVER===={RESET}")
        
        # 4. Beautifully print the grid with colors
        print(f"{CYAN}====================={RESET}")
        for r in range(9):
            if r > 0 and r % 3 == 0:
                print(f"{CYAN}------+-------+------{RESET}")
                
            row_str = []
            for c in range(9):
                if c > 0 and c % 3 == 0:
                    row_str.append(f"{CYAN}|{RESET}")
                
                # If it was empty originally, highlight it in GREEN
                if original_board[r][c] == '.':
                    row_str.append(f"{GREEN}{board[r][c]}{RESET}")
                else:
                    row_str.append(board[r][c])
                    
            print(" ".join(row_str))
        print(f"{CYAN}====================={RESET}")
    

obj1 = Solution()
obj2 = Solution2()

board =[["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]]

# for i in board:
#     print(i)

# obj.solveSudoku(board)

obj2.solveSudoku([[".",".",".",".",".",".",".",".","."],[".","9",".",".","1",".",".","3","."],[".",".","6",".","2",".","7",".","."],[".",".",".","3",".","4",".",".","."],["2","1",".",".",".",".",".","9","8"],[".",".",".",".",".",".",".",".","."],[".",".","2","5",".","6","4",".","."],[".","8",".",".",".",".",".","1","."],[".",".",".",".",".",".",".",".","."]])

# obj1.solveSudoku([[".",".",".",".",".",".",".",".","."],[".","9",".",".","1",".",".","3","."],[".",".","6",".","2",".","7",".","."],[".",".",".","3",".","4",".",".","."],["2","1",".",".",".",".",".","9","8"],[".",".",".",".",".",".",".",".","."],[".",".","2","5",".","6","4",".","."],[".","8",".",".",".",".",".","1","."],[".",".",".",".",".",".",".",".","."]])


# obj.solveSudoku([[".",".",".",".",".",".",".",".","."],[".",".",".",".","1",".",".","3","."],[".",".","6",".","2",".","7",".","."],[".",".",".","3",".","4",".",".","."],["2","1",".",".",".",".",".","9","8"],[".",".",".",".",".",".",".",".","."],[".",".","2","5",".","6","4",".","."],[".","8",".",".",".",".",".","1","."],[".",".",".",".",".",".",".",".","."]])
