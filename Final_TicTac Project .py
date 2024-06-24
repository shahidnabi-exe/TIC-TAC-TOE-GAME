import random


def play_game():
    print("Welcome to TicTacToe Game!")
    print("Main Menu:")
    print("For multiplayer player mode press 1")
    print("For single player mode press 2")
    print("To exit press any other key ")
    choice = input("Enter your choice: ")

    if choice == "1":
      play_multiplayer_game()
    elif choice == "2":
        play_single_player_game()   
    else:
        print("Goodbye!")

def display_board(board):
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i*3+j], "|", end=" ")
        print("\n-------------")


def check_win(board, player):
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]  
    ]
    for win in wins:
        if board[win[0]] == board[win[1]] == board[win[2]] == player:
            return True
    return False


def coin_toss():
    if random.randint(0, 1) == 0:
        return "Heads"
    else:
        return "Tails"


def make_move(board, position, symbol):
    if board[position - 1] == " ":
        board[position - 1] = symbol
        return True
    else:
        return False


def play_single_player_game():
    print("Welcome to Single Player TicTacToe Game!")
    player_symbol = input("Choose a symbol (X or O): ")
    computer_symbol = "O" if player_symbol == "X" else "X"

    board = [" "] * 9
    display_board(board)

    current_player = "Player"
    while True:
        if current_player == "Player":
            position = int(input("Enter your move (1-9): "))
            if make_move(board, position, player_symbol):
                display_board(board)
                if check_win(board, player_symbol):
                    print("Congratulations! You won!")
                    break
                if " " not in board:
                    print("It's a draw!")
                    break
                current_player = "Computer"
            else:
                print("Invalid move. Try again.")

        elif current_player == "Computer":
            position = random.randint(1, 9)
            while not make_move(board, position, computer_symbol):
                position = random.randint(1, 9)

            display_board(board)
            if check_win(board, computer_symbol):
                print("Computer wins!")
                break
            if " " not in board:
                print("It's a draw!")
                break
            current_player = "Player"

    play_again = input("Do you want to play again? (Yes/No): ")
    if play_again.upper() == "Yes":
        play_game()


def play_multiplayer_game():
    print("Welcome to Multiplayer TicTacToe Game!")
    player1_name = input("Enter Player 1 name: ")
    player2_name = input("Enter Player 2 name: ")
    player1_symbol = input(f"{player1_name}, choose a symbol (X or O): ")
    player2_symbol = "O" if player1_symbol == "X" else "X"

    board = [" "] * 9
    display_board(board)

    current_player = player1_name
    while True:
        position = int(input(f"{current_player}, enter your move (1-9): "))
        if make_move(board, position, player1_symbol if current_player == player1_name else player2_symbol):
            display_board(board)
            if check_win(board, player1_symbol):
                print(f"Congratulations {player1_name}! You won!")
                break
            if check_win(board, player2_symbol):
                print(f"Congratulations {player2_name}! You won!")
                break
            if " " not in board:
                print("It's a draw!")
                break
            current_player = player2_name if current_player == player1_name else player1_name
        else:
            print("Invalid move. Try again.")

    play_again = input("Do you want to play again? (Yes/No): ")
    if play_again.upper() == "Yes":
        play_game()


play_game()