from stockfish import Stockfish
from datetime import date
import chess.pgn
import chess

thinking = 2000
play = input("Do you want to play? (y/n): ")

if play == 'yes' or play == 'y':
    file = open('game.pgn', 'a')
    file.truncate(0)
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
    order = ["Human player", "Stockfish"]
elif color == 'black' or color == 'b':
    half = half + 1
    order = ["Stockfish", "Human player"]

    print('Starting game...')
    first_move = stockfish.get_best_move_time(thinking)
    print(f'White moves: {board.san(chess.Move.from_uci(first_move))}')
    board.push_uci(first_move)
    moves.append(first_move)
    file.write(f'{first_move}\n')
else:
    print('\nPlease enter yes or no')

try:
    while True:
        human_move = input("Your move: ")
        
        #if half == 0: main = pgn.add_main_variation(board.parse_san(human_move))
        #else: main = main.add_main_variation(board.parse_san(human_move))

        while True:
            try:
                moves.append(str(board.parse_san(human_move)))
                board.push_san(human_move)
            except ValueError:
                print(human_move, 'is not a legal move!')
                human_move = input("Your move: ")
            else:
                break

        stockfish.set_position(moves)
        computer_move = stockfish.get_best_move_time(thinking)
        print(f'Computer moves: {board.san(chess.Move.from_uci(computer_move))}')

        #main = main.add_main_variation(chess.Move.from_uci(computer_move))
        moves.append(computer_move)
        board.push_uci(computer_move)
        file.write(f'{computer_move}\n')
except KeyboardInterrupt:
    file.close()
    print('\nQuiting...')