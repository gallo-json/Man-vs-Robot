from stockfish import Stockfish
from datetime import date
import chess

play = input("Do you want to play? (y/n): ")

if play == 'yes' or play == 'y':
    pgn = open('../game.pgn', 'w')
    pgn.write(f'[Date {date.today().strftime("%m/%d/%y")}]\n')

    stockfish = Stockfish('/usr/games/stockfish')
    board = chess.Board()
elif play == 'no' or play == 'n':
    exit(0)
else:
    print('\nPlease enter yes or no')

color = input("What color do you want to be? ")


if color == 'white' or color == 'w':
    print('Starting game...')
    pgn.writelines(['[White "Human player"]', '[Black "Stockfish"]'])
elif color == 'black' or color == 'b':
    print('Starting game...')
    first_move = stockfish.get_best_move()
    print(f'White moves: {board.san(chess.Move.from_uci(first_move))}')
    board.push_uci(first_move)
    pgn.writelines(['[White "Stockfish"]', '[Black "Human player"]'])
else:
    print('\nPlease enter yes or no')
