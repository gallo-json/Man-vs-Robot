from stockfish import Stockfish
from datetime import date
import chess.pgn
import chess

thinking = 2000
play = input("Do you want to play? (y/n): ")

if play == 'yes' or play == 'y':
    game = open('game.pgn', 'w')
    pgn = chess.pgn.Game()
    pgn.headers["Event"] = "Example"

    #pgn.write(f'[Date {date.today().strftime("%m/%d/%y")}]\n')

    stockfish = Stockfish('/usr/games/stockfish')
    board = chess.Board()
elif play == 'no' or play == 'n':
    exit(0)
else:
    print('\nPlease enter yes or no')

color = input("What color do you want to be? ")

half = 0
moves = []

if color == 'white' or color == 'w':
    print('Starting game...')
    pgn.headers["White"] = "Human player"
    pgn.headers["Black"] = "Stockfish"
elif color == 'black' or color == 'b':
    half = half + 1
    pgn.headers["White"] = "Stockfish"
    pgn.headers["Black"] = "Human player"

    print('Starting game...')
    first_move = stockfish.get_best_move_time(thinking)
    print(f'White moves: {board.san(chess.Move.from_uci(first_move))}')
    main = pgn.add_main_variation(chess.Move.from_uci(first_move))
    board.push_uci(first_move)
    moves.append(first_move)
else:
    print('\nPlease enter yes or no')

while True:
    human_move = input("Your move: ")
    
    if half == 0: main = pgn.add_main_variation(chess.Move.from_uci(human_move))
    else: main = main.add_main_variation(chess.Move.from_uci(human_move))

    moves.append(str(board.parse_san(human_move)))
    board.push_san(human_move)
    
    stockfish.set_position(moves)
    computer_move = stockfish.get_best_move_time(thinking)
    print(f'Computer moves: {board.san(chess.Move.from_uci(computer_move))}')

    board.push_uci(computer_move)
    moves.append(computer_move)
    break
print(moves)
print(pgn)