from stockfish import Stockfish
from datetime import date
import chess

play = input("Do you want to play? (y/n): ")

while play not in ['yes', 'y', 'no', 'n']:
	if play == 'yes' or play == 'y':
		pgn = open('../game.pgn', 'w')
        pgn.write(f'[Date {date.today().strftime("%m/%d/%y")}]\n')
		break
	elif play == 'no' or play == 'n':
		exit(0)
	else:
		print('\nPlease enter yes or no')

color = input("What color do you want to be? ")

while answer not in ['white', 'w', 'black', 'b']:
	if color == 'white' or color == 'w':
		pgn.writelines(['[White "Human player"]', '[Black "Stockfish"]'])
		break
	elif color == 'black' or color == 'b':
		pgn.writelines(['[White "Stockfish"]', '[Black "Human player"]'])
        break
	else:
		print('\nPlease enter yes or no')

#stockfish = Stockfish('/usr/games/stockfish')