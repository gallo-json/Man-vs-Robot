from stockfish import Stockfish
from datetime import date
from ser import Ser
import chess.pgn
import chess

thinking = 2000
play = input("Do you want to play? (y/n): ")

while True:
    if play == 'yes' or play == 'y':
        file = open('game.pgn', 'a')
        file.truncate(0)
        pgn = chess.pgn.Game()

        stockfish = Stockfish('/usr/games/stockfish')
        board = chess.Board()
        break
    elif play == 'no' or play == 'n':
        exit(0)
    else:
        print('Please enter yes or no')
        play = input("Do you want to play? (y/n): ")

color = input("What color do you want to be? ")

moves = []
order = []

while True:
    if color == 'white' or color == 'w':
        order = ["Human player", "Stockfish"]
        print('Starting game...')
        break
    elif color == 'black' or color == 'b':
        order = ["Stockfish", "Human player"]
        print('Starting game...')
        first_move = stockfish.get_best_move_time(thinking)
        print(f'White moves: {board.san(chess.Move.from_uci(first_move))}')
        board.push_uci(first_move)
        moves.append(first_move)
        break
    else:
        print('Please enter white (w) or black (b)')
        color = input("What color do you want to be? ")

try:
    while True:
        resign = False
        human_move = input("Your move: ")

        while True:
            try:
                moves.append(str(board.parse_san(human_move)))
                board.push_san(human_move)
            except ValueError:
                print(human_move, 'is not a legal move!')
                human_move = input("Your move: ")
            else:
                break

        if board.is_check():
            print('Computer is in check!')

        if board.is_checkmate():
            print('You checkmated stockfish, you win!')
            break
        elif board.is_stalemate():
            print('Game is a stalemate.')
            break
        elif board.is_insufficient_material():
            print('Insufficient material to win.')
            break
        elif board.is_fivefold_repetition():
            print('Fivefold repetition - game is a draw.')
        elif resign:
            print('You resigned the game. Stockfish wins.')
            break 

        stockfish.set_position(moves)
        computer_move = stockfish.get_best_move_time(thinking)
        print(f'Computer moves: {board.san(chess.Move.from_uci(computer_move))}')

        moves.append(computer_move)
        board.push_uci(computer_move)

        if board.is_check():
            print('You are in check!')

        if len(computer_move) == 5:
            print("Please promote my pawn into a", computer_move[-1].upper())

        if board.is_checkmate():
            print('Stockfish checkmated you. You lose.')
            break
        elif board.is_stalemate():
            print('Game is a stalemate.')
            break
        elif board.is_insufficient_material():
            print('Insufficient material to win.')
            break
        elif board.is_fivefold_repetition():
            print('Fivefold repetition - game is a draw.')

    pgn.from_board(board)
    pgn.headers["Date"] = date.today().strftime("%m/%d/%y")
    pgn.headers["White"] = order[0]
    pgn.headers["Black"] = order[1]

    print('Result:', board.result())

    file.truncate(0)
    file.write(pgn)
    file.close()
except KeyboardInterrupt:
    file.close()
    print('\nQuiting...')