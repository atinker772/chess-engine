import chess
from engine.search import AlphaBetaPlayer

def test_finds_mate_in_one():
    board = chess.Board("r1bqkb1r/pppp1ppp/2n2n2/4p2Q/2B1P3/8/PPPP1PPP/RNB1K1NR w KQkq - 4 4")
    assert AlphaBetaPlayer(depth=2).choose_move(board) == chess.Move.from_uci("h5f7")

def test_does_not_hang_queen_for_pawn():
    board = chess.Board("4k3/4p3/3p4/8/8/8/8/3QK3 w - - 0 1")
    assert AlphaBetaPlayer(depth=2).choose_move(board) != chess.Move.from_uci("d1d6")
