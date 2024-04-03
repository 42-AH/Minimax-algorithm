import math


def evaluate(board):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:
            if board[row][0] == 'X':
                return 10
            elif board[row][0] == 'O':
                return -10
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == 'X':
                return 10
            elif board[0][col] == 'O':
                return -10
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'X':
            return 10
        elif board[0][0] == 'O':
            return -10
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'X':
            return 10
        elif board[0][2] == 'O':
            return -10
    for row in range(3):
        for col in range(3):
            if board[row][col] is None:
                return None
    return 0

def minimax(board, depth, is_maximizing):
    
    score = evaluate(board)
    if score is not None:
        return score
    if depth == 0:
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] is None:
                    board[row][col] = 'X'
                    eval = minimax(board, depth - 1, False)
                    max_eval = max(max_eval, eval)
                    board[row][col] = None
        return max_eval
    else:
        min_eval = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] is None:
                    board[row][col] = 'O'
                    eval = minimax(board, depth - 1, True)
                    min_eval = min(min_eval, eval)
                    board[row][col] = None
        return min_eval

def find_best_move(board):
    best_eval = -math.inf
    best_move = None

    for row in range(3):
        for col in range(3):
            if board[row][col] is None:
                board[row][col] = 'X'
                eval = minimax(board, original_depth, False)
                board[row][col] = None
                if eval > best_eval:
                    best_eval = eval
                    best_move = (row, col)

    return best_move

def print_board(board):

    for row in range(len(board)):
        one = (str(board[row][0])) 
        two = (str(board[row][1]))
        three = (str(board[row][2]))
        if one == "None":
          one = " "
        if two == "None":
          two = " "
        if three == "None":
          three = " "
        print(one + two + three)

board = [[None, None, None],
         [None, None, None],
         [None, None, None]]

print_board(board)
global original_depth
original_depth = int(input("Depth: "))
while evaluate(board) is None:
    human_move = input("Enter your move (row,col): ")
    row, col = map(int, human_move.split(","))
    if board[row][col] is None:
        board[row][col] = 'O' 
        print("Your Move:")
        print_board(board)
        if evaluate(board) is not None:
            break

        print("AI's Move:")
        ai_move = find_best_move(board)
        board[ai_move[0]][ai_move[1]] = 'X'
        print_board(board)
    else:
        print("Illegal move. Try again")

result = evaluate(board)
if result == 10:
    print("You lose")
elif result == -10:
    print("You win")
else:
    print("It's a draw")
