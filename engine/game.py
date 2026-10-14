import chess

def play_game(white, black, max_moves=300, verbose=False):
    board = chess.Board()
    while not board.is_game_over() and board.fullmove_number < max_moves:
        player = white if board.turn == chess.WHITE else black
        board.push(player.choose_move(board))
        if verbose:
            print(board, "\n")
    return board.result(claim_draw=True), board
