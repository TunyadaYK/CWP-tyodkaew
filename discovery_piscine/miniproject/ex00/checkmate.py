def is_valid_position(board_size, row, col):
    return 0 <= row < board_size and 0 <= col < board_size


def checkmate(board_text):
    if not isinstance(board_text, str):
        return

    board_rows = [line for line in board_text.strip('\n').split('\n') if line]
    if not board_rows:
        return

    board_size = len(board_rows)
    king_position = None
    king_count = 0
    valid_pieces = {'K', 'Q', 'R', 'B', 'P'}

    for row_index, line in enumerate(board_rows):
        if len(line) != board_size:
            return 
        for col_index, piece in enumerate(line):
            if piece == 'K':
                king_position = (row_index, col_index)
                king_count += 1

    if king_count != 1:
        return

    king_row, king_col = king_position

    ray_directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),    
        (-1, -1), (-1, 1), (1, -1), (1, 1)  
    ]

    for direction_index, (row_offset, col_offset) in enumerate(ray_directions):
        current_row = king_row + row_offset
        current_col = king_col + col_offset

        while is_valid_position(board_size, current_row, current_col):
            piece = board_rows[current_row][current_col]

            if piece in valid_pieces:
                is_diagonal_search = direction_index >= 4

                if is_diagonal_search:
                    if piece in ('B', 'Q'):
                        print("Success")
                        return
                else:
                    if piece in ('R', 'Q'):
                        print("Success")
                        return

                break

            current_row += row_offset
            current_col += col_offset

    pawn_attack_positions = [
        (king_row + 1, king_col - 1),
        (king_row + 1, king_col + 1)
    ]

    for pawn_row, pawn_col in pawn_attack_positions:
        if is_valid_position(board_size, pawn_row, pawn_col) and board_rows[pawn_row][pawn_col] == 'P':
            print("Success")
            return

    print("Fail")