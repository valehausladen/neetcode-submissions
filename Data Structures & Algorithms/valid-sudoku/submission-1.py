class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [i for i in range(9)]
        columns = rows[:]
        # Check rows:
        for row in rows:
            seen = set()
            for column in columns:
                if board[row][column] != ".":
                    if board[row][column] not in seen:
                        seen.add(board[row][column])
                    else:
                        return False
        # Check columns
        for column in columns:
            seen = set()
            for row in rows:
                if board[row][column] != ".":
                    if board[row][column] not in seen:
                        seen.add(board[row][column])
                    else:
                        return False
        # Check sub boxes
        sub_boxes_columns = [i for i in range(3)]
        sub_boxes_rows = sub_boxes_columns[:]
        columns = sub_boxes_columns[:]
        rows = sub_boxes_columns[:]
        for sub_boxes_row in sub_boxes_rows:
            for sub_boxes_column in sub_boxes_columns:
                seen = set()
                for row in rows:
                    for column in columns:
                        if board[sub_boxes_row*3+row][sub_boxes_column*3+column] != ".":
                            if board[sub_boxes_row*3+row][sub_boxes_column*3+column] not in seen:
                                seen.add(board[sub_boxes_row*3+row][sub_boxes_column*3+column])
                            else:
                                return False
        return True



