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
                elem = int(elem) # range betweeen [1,9]

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