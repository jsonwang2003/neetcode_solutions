"""
You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false
"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                elem = board[row][col]
                if elem == ".":
                    continue

                if elem in cols[col]:
                    return False
                if elem in rows[row]:
                    return False
                
                if elem in boxes[row // 3][col // 3]:
                    return False
                
                # add elem to sets
                cols[col].add(elem)
                rows[row].add(elem)
                boxes[row // 3][col // 3].add(elem)

        return True