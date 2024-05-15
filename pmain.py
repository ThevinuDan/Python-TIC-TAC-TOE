board = [
  0,0,0,
  0,0,0,
  0,0,0
  ]

print('Welcome To Tic Tac Toe Terminal')

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
while turn <= 9:
  print('Player 1 input row and column')
  p1_position = int(input("Enter position number (1 through 9): ")) - 1
  if board[p1_position] == 0:
    board[p1_position] = 1
  elif board[p1_position] == 2:
    print('player 2 has already placed their mark here')
  else:
    print('invalid place number or place already taken')
  print_board()
  turn += 1
  player_1_stat = check_win(1)
  if player_1_stat == True:
    print('player 1 wins')
    break
  print('Player 2 input row and column')
  p2_position = int(input("Enter position number (1 through 9): ")) - 1
  if board[p2_position] == 0:
    board[p2_position] = 2
  elif board[p2_position] == 1:
    print('player 1 has already placed their mark here')
  else:
    print('invalid place number or place already taken')
  print_board()
  turn += 1
  player_2_stat = check_win(2)
  if player_2_stat == True:
    print('player 2 wins')
    break


    
