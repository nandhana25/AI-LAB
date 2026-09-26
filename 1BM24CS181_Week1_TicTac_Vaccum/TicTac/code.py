import random

def display_board(board):
    print("\n")
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---|---|---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---|---|---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_winner(board, player):
    winning_positions = [
        (0, 1, 2),  
        (3, 4, 5), 
        (6, 7, 8),  
        (0, 3, 6),  
        (1, 4, 7),  
        (2, 5, 8),  
        (0, 4, 8),  
        (2, 4, 6)   
    ]

    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] == player:
            return True

    return False


def board_full(board):
    return all(cell != " " for cell in board)
def computer_move(board):
    empty_cells = [i for i in range(9) if board[i] == " "]

    if empty_cells:
        return random.choice(empty_cells)

    return -1


def tic_tac_toe():
    board = [" "] * 9

    human = "X"
    computer = "O"

    print("===== TIC-TAC-TOE =====")
    print("You are X")
    print("Computer is O")

    print("\nCell numbers:")
    print(" 1 | 2 | 3 ")
    print("---|---|---")
    print(" 4 | 5 | 6 ")
    print("---|---|---")
    print(" 7 | 8 | 9 ")

    turn = random.choice(["human", "computer"])

    while True:
        display_board(board)

        if turn == "human":
            try:
                position = int(input("Enter a position (1-9): ")) - 1

                if position < 0 or position > 8:
                    print("Invalid position! Choose between 1 and 9.")
                    continue

                if board[position] != " ":
                    print("That position is already occupied!")
                    continue

                board[position] = human

                if check_winner(board, human):
                    display_board(board)
                    print("Congratulations! You won!")
                    break

                if board_full(board):
                    display_board(board)
                    print("It's a draw!")
                    break

                turn = "computer"

            except ValueError:
                print("Please enter a number between 1 and 9.")

        else:
            print("Computer is making a move...")

            position = computer_move(board)
            board[position] = computer

            if check_winner(board, computer):
                display_board(board)
                print("Computer wins!")
                break

            if board_full(board):
                display_board(board)
                print("It's a draw!")
                break

            turn = "human"
tic_tac_toe()
