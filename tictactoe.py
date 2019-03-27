import random

def display_board(board):
	#clear board
	print('\n' * 100)
	print(f'      {board[1]} | {board[2]} | {board[3]}') 
	print('     ----------')
	print(f'      {board[4]} | {board[5]} | {board[6]}') 
	print('     ----------')
	print(f'      {board[7]} | {board[8]} | {board[9]}') 
 
#Assign player markers
def player_input():
	marker = ''

	while not (marker == 'X' or marker == 'O'):
		marker = input('Player 1: Do you want to be X or O ').upper()

		if marker == 'X':
			return('X', 'O')
		else:
			return('O', 'X')

def place_marker(board, marker, position):
	board[position] = marker

def win_check(board, marker):
	return(
		#check all rows
		(board[1] == board[2] == board[3] == marker) or 
		(board[4] == board[5] == board[6] == marker) or
		(board[7] == board[8] == board[9] == marker) or
		# check all columns
		(board[1] == board[4] == board[7] == marker) or
		(board[2] == board[5] == board[8] == marker) or
		(board[3] == board[6] == board[9] == marker) or
		#Check diagonals
		(board[1] == board[5] == board[9] == marker) or
		(board[7] == board[5] == board[3] == marker)
	)
def choose_first():
	if random.randint(0,1) == 0:
		return 'Player 2'
	else:
		return 'Player 1'

def space_check(board, position):
	return board[position] == ' '

def check_full_board(board):
	for space in board:
		if space == ' ':
			return False
		else:
			return True

def player_choice(board):
	position = int(input('Choose a position: (1 - 9) '))
	if space_check(board, position):
		return position
	else:
		print('Space is taken! Try again!')
		return player_choice(game_board)
	'''
	position = 0

	while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
		position = int(input('Choose a position: (1 - 9) '))
		return position
	'''

def replay():
	choice = input('Play again?  Enter Yes or No ').upper()

	return choice == 'YES'

# Keep running game
print('Welcome to Tic Tac Toe')

while True:
	#Play game
	# Set up game (board, first player, chose markers)
	game_board = [' '] * 10

	player1_marker, player2_marker = player_input()
	turn = choose_first()

	print(f'{turn} will go first')

	play_game = input('Ready to play? Yes or No').upper()

	if play_game == 'YES':
		game_rdy = True
	else:
		game_rdy = False

	while game_rdy:
		if turn == 'Player 1':
			#show bord
			display_board(game_board)
			position = player_choice(game_board)
			place_marker(game_board, player1_marker, position)

			if win_check(game_board, player1_marker):
				display_board(game_board)
				print('Player 1 has won!!')
				game_rdy = False
			else:
				if check_full_board(game_board):
					display_board(game_board)
					print('Tie Game')
					game_on = False
				else:
					turn = 'Player 2'
		else:
			#show bord
			display_board(game_board)
			position = player_choice(game_board)
			place_marker(game_board, player2_marker, position)

			if win_check(game_board, player2_marker):
				display_board(game_board)
				print('Player 2 has won!!')
				game_rdy = False
			else:
				if check_full_board(game_board):
					display_board(game_board)
					print('Tie Game')
					game_on = False
				else:
					turn = 'Player 1'

	if not replay():
		break
# Break loop in replay function