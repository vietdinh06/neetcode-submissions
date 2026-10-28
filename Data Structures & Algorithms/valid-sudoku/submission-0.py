class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashed_sub = {}

        for row in range(len(board)):

            hashed_row = set()
            hashed_col = set()
            for col in range(len(board[row])):
                row_spot = board[row][col]
                col_spot = board[col][row]

                if row_spot != '.':
                    if row_spot in hashed_row:
                        return False
                    else :
                        hashed_row.add(row_spot)

                if col_spot != '.':
                    if col_spot in hashed_col:
                        return False
                    else :
                        hashed_col.add(col_spot)

                point = (row//3, col//3)
                if point not in hashed_sub:
                    hashed_sub[point] = set()

                if row_spot != '.':
                    if row_spot in hashed_sub[point]:
                        return False
                    else:
                        hashed_sub[point].add(row_spot)

        return True
    
