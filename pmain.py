print(''' 
*******************************
*   Welcome to Tic-Tac-Toe!   *
*                             *
*    Let the Battle Begin!    *
*******************************
-------------------------------
Rules:
    Player 1 is X, Player 2 is O.
    Enter the number corresponding to the positions shown on the board below:

 ______________
|  1 |  2 |  3 |
|____|____|____|
|  4 |  5 |  6 |
|____|____|____|  
|  7 |  8 |  9 |
|____|____|____|        

Example: If you want to place your symbol in the top-right corner, enter "3".

How to Win:
    To win, you must get three of your symbols in a row, column, or diagonal.
      
Draw:
    If all positions on the board are filled and no player has won, the game ends in a draw.
-------------------------------
*******************************
       Enjoy the game!
*******************************
''')
  
board = [
  0,0,0,
  0,0,0,
  0,0,0
  ]

def print_board():
  display_positon = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
  for i in range(9):
    if board[i] == 1:
      display_positon[i] = 'X'
    elif board[i] == 2:
      display_positon[i] = 'O'

  print('''
 ______________
|  {} |  {} |  {} |
|____|____|____|
|  {} |  {} |  {} |
|____|____|____|  
|  {} |  {} |  {} |
|____|____|____|        

'''.format(*display_positon))    
  

def check_win(num):
    if board[0] == num and board[1] == num and board[2] == num:
      return True
    elif board[3] == num and board[4] == num and board[5] == num:
      return True
    elif board[6] == num and board[7] == num and board[8] == num:
      return True
    elif board[0] == num and board[3] == num and board[6] == num:
      return True
    elif board[1] == num and board[4] == num and board[7] == num:
      return True
    elif board[2] == num and board[5] == num and board[8] == num:
      return True
    elif board[0] == num and board[4] == num and board[8] == num:
      return True
    elif board[2] == num and board[4] == num and board[6] == num:
      return True
    else:
      return False

turn = 0

while turn < 9:
    while True:
        try:
            p1_position = int(input("Player 1 enter position number (1 through 9): ")) - 1
            if 0 <= p1_position <= 8 and board[p1_position] == 0:
                board[p1_position] = 1
                break
            elif p1_position < 0 or p1_position > 8:
                print('Invalid position number. Please enter a number between 1 and 9.')
            else:
                print('Position already taken. Please choose another position.')
        except ValueError:
            print('Invalid input. Please enter a number.')

    turn += 1
    print_board()

    if turn == 9:
        print('Draw')
        break

    player_1_stat = check_win(1)
    if player_1_stat:
        print('Player 1 WINS')
        break

    while True:
        try:
            p2_position = int(input("Player 2 enter position number (1 through 9): ")) - 1
            if 0 <= p2_position <= 8 and board[p2_position] == 0:
                board[p2_position] = 2
                break
            elif p2_position < 0 or p2_position > 8:
                print('Invalid position number. Please enter a number between 1 and 9.')
            else:
                print('Position already taken. Please choose another position.')
        except ValueError:
            print('Invalid input. Please enter a number.')

    turn += 1
    print_board()

    player_2_stat = check_win(2)
    if player_2_stat:
        print('Player 2 WINS')
        break
