# A 2D Array is essentially an "array of arrays." If a 1D array is a straight line of items, a 2D array is a grid or a table with rows and columns.

# In memory, even though we visualize it as a square grid, the computer still stores it as one long contiguous line. It just uses math to figure out where each "row" starts.
# 2 * 3 matrix
# matrix = [
#     [1, 2, 3], # Row 0
#     [4, 5, 6], # Row 1
#     [7, 8, 9]  # Row 2
# ]

# # print(matrix[0])

# for row in matrix:
#     for column in row:
#         print(column, end=" ")
#     print('')

from typing import List, Optional

# Create a 2D array and all operations
class TwoDimensionsMatrix:
    metrix = [[None]]
   
    def __init__(self, rows, cols) -> None:
        self.matrix: List[List[Optional[int]]] = [[None for _ in range(cols)] for _ in range(rows)]
        self.rows = rows
        self.cols = cols

    def print_matrix(self):
        print("\n--- Current Values ---")
        for row in self.matrix:
            # Use join to make it look cleaner
            print(" | ".join(str(item) for item in row))

    def show_positions(self):
        print(f"\n--- Matrix Grid Layout ({self.rows}x{self.cols}) ---")
        
        # Calculate the width needed for each "cell" based on index size
        cell_width = len(f"{self.rows},{self.cols}") + 2
        horizontal_line = "-" * (self.cols * (cell_width + 1) + 1)

        for r in range(self.rows):
            print(horizontal_line)
            for c in range(self.cols):
                # Using f-string formatting to center the coordinates
                position = f"{r},{c}"
                print(f"|{position.center(cell_width)}", end="")
            print("|")
        print(horizontal_line)

    def add_value_to_position(self, position: str, value=12):
        try:
            # 1. Clean up whitespace and split
            parts = position.split(",")
            if len(parts) != 2:
                raise ValueError("Position must be in 'row,col' format.")

            row = int(parts[0].strip())
            col = int(parts[1].strip())

            # 2. Check the "Bounds" (Is it inside the grid?)
            # Indices must be >= 0 and < total rows/cols
            if 0 <= row < self.rows and 0 <= col < self.cols:
                self.matrix[row][col] = value
                print(f"Successfully added {value} at ({row}, {col})")
            else:
                print(f"Error: Position ({row}, {col}) is out of bounds for {self.rows}x{self.cols} matrix.")

        except ValueError:
            print("Error: Please provide valid integers separated by a comma (e.g., '1,2').")

    def rotate_90_clockwise(self):
        # 1. Transpose: Swap matrix[i][j] with matrix[j][i]
        for i in range(self.rows):
            # We start j from 'i' so we don't swap elements back to their original spots
            for j in range(i + 1, self.cols):
                self.matrix[i][j], self.matrix[j][i] = self.matrix[j][i], self.matrix[i][j]

        # 2. Reverse each row
        for row in self.matrix:
            row.reverse()


two_d_arr = TwoDimensionsMatrix(3,3)

# two_d_arr.print_matrix()
two_d_arr.show_positions()
two_d_arr.add_value_to_position("1,2",23)
two_d_arr.print_matrix()
two_d_arr.rotate_90_clockwise()
two_d_arr.print_matrix()
two_d_arr.show_positions()