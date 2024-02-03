import random
import os.path
import json
random.seed()




def draw_board(board):
    print(" ",end="")
    print("-"*11)
    for row in board:
        print("| ",end="")
        print(" | ".join(row),end="")
        print(" |")
        print(" ",end="")
        print("-"*11)
        

def welcome(board):
    print("Welcome to Noughts and Crosses!")
    draw_board(board)


def initialise_board(board):
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '
    return board
    
    
    
def get_player_move(board):
    while True:
        try:
            move = int(input("Enter the cell number to place 'X': "))
            if move >=1 and move <=9:
                #since there are three elements in a row //3 
                #the index starts at 0 so move-1
                row = (move - 1) // 3
                col = (move - 1) % 3
                if board[row][col] == ' ':
                    return row, col
                else:
                    print("Cell already occupied. Choose another.")
            else:
                print("Invalid input. Enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")
            
            

def choose_computer_move(board):
    while True:
        move=random.randint(1,9)
        row = (move - 1) // 3
        col = (move - 1) % 3
        if board[row][col] == ' ':
            return row, col    


def check_for_win(board, mark):
    # develop code to check if either the player or the computer has won
    # return True if someone won, False otherwise
    
    if (board[0][0] == mark and board[0][1] == mark and board[0][2] == mark) or \
   (board[1][0] == mark and board[1][1] == mark and board[1][2] == mark) or \
   (board[2][0] == mark and board[2][1] == mark and board[2][2] == mark) or \
   (board[0][0] == mark and board[1][0] == mark and board[2][0] == mark) or \
   (board[0][1] == mark and board[1][1] == mark and board[2][1] == mark) or \
   (board[0][2] == mark and board[1][2] == mark and board[2][2] == mark) or \
   (board[0][0] == mark and board[1][1] == mark and board[2][2] == mark) or \
   (board[0][2] == mark and board[1][1] == mark and board[2][0] == mark):
        return True
    else:
        return False


def check_for_draw(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

        
def play_game(board):
    initialise_board(board)
    draw_board(board)
    while True:
        row, col = get_player_move(board)
        board[row][col] = 'X'
        draw_board(board)

        if check_for_win(board, 'X'):
            return 1
        elif check_for_draw(board):
            return 0

        row, col = choose_computer_move(board)
        board[row][col] = 'O'
        draw_board(board)

        #if computer wins reduce the score by 1
        if check_for_win(board, 'O'):
            return -1
        elif check_for_draw(board):
            return 0
                    
                
def menu():
    print("1 - Play the game")
    print("2 - Save score in file 'leaderboard.txt'")
    print("3 - Load and display the scores from 'leaderboard.txt'")
    print("q - End the program")
    choice = input("Enter your choice: ")
    return choice


def load_scores():
    leaders = {}
    try:
        with open('leaderboard.txt', 'r') as file:
            leaders = json.load(file)
    except FileNotFoundError:
        print("Leaderboard file not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON. Leaderboard file may be corrupted.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return leaders


def save_score(score):
    name = input("Enter your name: ")
    leaders = load_scores()
    
    if not name.isalpha() or not str(score).isdigit():
        print("Invalid input. Please enter a valid name and score.")
        return
    
    if name in leaders:
        leaders[name] += score
    else:
        leaders[name] = score
    
    try:
        with open('leaderboard.txt', 'w') as file:
            json.dump(leaders, file)
        print("Score saved successfully.")
    except Exception as e:
        print(f"An error occurred while saving the score: {e}")


def display_leaderboard(leaders):
    print("Leaderboard:")
    if not leaders:
        print("No scores available.")
    else:
        for name, score in leaders.items():
            print(f"{name}: {score}")