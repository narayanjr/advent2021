from collections import defaultdict


def read_file():
    boards = []

    with open("Day 4/data.txt") as f:
        lines = [line.strip() for line in f.readlines()]
        draw_sequence = lines[0].split(",")

        lines = lines[2:]
        board = []
        for line in lines:
            if line == "":
                boards.append(board)
                board = []
                continue
            else:
                board.append(line.split())

    return draw_sequence, boards


def did_board_win(board, last_r, last_c):
    return (
        board[last_r][0]
        + board[last_r][1]
        + board[last_r][2]
        + board[last_r][3]
        + board[last_r][4]
        == 5
        or board[0][last_c]
        + board[1][last_c]
        + board[2][last_c]
        + board[3][last_c]
        + board[4][last_c]
        == 5
    )


def sum_board(board, drawn_board):
    board_sum = 0
    for idr, row in enumerate(drawn_board):
        for idc, col_val in enumerate(row):
            board_sum = board_sum + (int(board[idr][idc]) if col_val == 0 else 0)
    return board_sum


def calc_draws_and_sum_to_win(sequence, board, current_min_draws):
    drawn_board = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]

    for ids, draw in enumerate(sequence):
        for idr, row in enumerate(board):
            for idc, col_val in enumerate(row):
                if col_val == draw:
                    drawn_board[idr][idc] = 1
                    if did_board_win(drawn_board, idr, idc):
                        return ids, int(draw) * sum_board(board, drawn_board)

        if ids > current_min_draws:
            break

    return 999999, 999999


sequnce, boards = read_file()
current_min_draws = 99999
winning_answer = 0

for board in boards:
    draws, calced_answer = calc_draws_and_sum_to_win(sequnce, board, current_min_draws)
    winning_answer = calced_answer if draws < current_min_draws else winning_answer
    current_min_draws = min(current_min_draws, draws)


print(f"winning_answer: {winning_answer}")
