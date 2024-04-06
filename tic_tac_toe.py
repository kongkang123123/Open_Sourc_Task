import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]]
    ]
    return [player, player, player] in win_conditions

def get_free_positions(board):
    positions = []
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == " ":
                positions.append((i, j))
    return positions

def player_move(board):
    positions = get_free_positions(board)
    move = -1, -1
    while move not in positions:
        try:
            move = tuple(map(int, input("당신의 차례입니다. 위치를 선택하세요 (행 열): ").split()))
        except ValueError:
            pass
    return move

def computer_move(board):
    positions = get_free_positions(board)
    return random.choice(positions)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]  # X가 사용자, O가 컴퓨터
    turn = 0

    while True:
        print_board(board)
        if turn % 2 == 0:
            row, col = player_move(board)
            board[row][col] = "X"
        else:
            print("컴퓨터의 차례입니다.")
            row, col = computer_move(board)
            board[row][col] = "O"
            print(f"컴퓨터는 ({row}, {col})에 놓았습니다.")

        if check_win(board, players[turn % 2]):
            print_board(board)
            if turn % 2 == 0:
                print("축하합니다! 당신이 이겼습니다!")
            else:
                print("컴퓨터가 이겼습니다.")
            break

        if all(cell != " " for row in board for cell in row):
            print_board(board)
            print("무승부입니다!")
            break

        turn += 1

if __name__ == '__main__':
    tic_tac_toe()
