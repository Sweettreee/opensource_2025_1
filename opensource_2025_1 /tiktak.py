import random

# 틱택토 보드 출력 함수
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# 승리 조건 확인 함수
def check_winner(board, player):
    # 행, 열, 대각선 확인
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# 빈 칸 확인 함수
def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

# 컴퓨터의 움직임 선택 함수
def computer_move(board):
    empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]
    return random.choice(empty_cells)

# 틱택토 메인 함수
def tic_tac_toe():
    print("틱택토 게임 시작!")
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"  # 사람은 X, 컴퓨터는 O

    while True:
        print_board(board)
        
        # 사람의 턴
        try:
            row, col = map(int, input("당신의 턴 (행 열 입력, 예: 0 1): ").split())
            if board[row][col] != " ":
                print("이미 선택된 위치입니다. 다시 시도하세요.")
                continue
            board[row][col] = player
        except (ValueError, IndexError):
            print("잘못된 입력입니다. 다시 시도하세요.")
            continue
