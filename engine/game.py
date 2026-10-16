import chess
import random

def play_game(white, black, max_moves=300, verbose=False, random_opening_plies=0):
    board = chess.Board()
    for _ in range(random_opening_plies):
        if board.is_game_over():
            break
        board.push(random.choice(list(board.legal_moves)))
    while not board.is_game_over(claim_draw=True) and board.fullmove_number < max_moves:
        player = white if board.turn == chess.WHITE else black
        board.push(player.choose_move(board))
        if verbose:
            print(board, "\n")
    return board.result(claim_draw=True), board
