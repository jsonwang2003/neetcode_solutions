"""
You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false
"""


class Solution:
    def box_index(self, row: int, col: int) -> int:
        if row in {0, 1, 2} and col in {0, 1, 2}:
            return 0
        if row in {0, 1, 2} and col in {3, 4, 5}:
            return 1
        if row in {0, 1, 2} and col in {6, 7, 8}:
            return 2
        if row in {3, 4, 5} and col in {0, 1, 2}:
            return 3
        if row in {3, 4, 5} and col in {3, 4, 5}:
            return 4
        if row in {3, 4, 5} and col in {6, 7, 8}:
            return 5
        if row in {6, 7, 8} and col in {0, 1, 2}:
            return 6
        if row in {6, 7, 8} and col in {3, 4, 5}:
            return 7
        if row in {6, 7, 8} and col in {6, 7, 8}:
            return 8

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                elem = board[row][col]
                if elem == ".":
                    continue

                if elem in cols[col]:
                    return False
                if elem in rows[row]:
                    return False
                
                box_num = self.box_index(row, col)
                if elem in boxes[box_num]:
                    return False
                
                # add elem to sets
                cols[col].add(elem)
                rows[row].add(elem)
                boxes[box_num].add(elem)

        return True