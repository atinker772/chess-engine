import chess
from engine.game import play_game
from engine.players import RandomPlayer
from engine.search import AlphaBetaPlayer
from engine.evaluate import material_eval

def arena(player_a, player_b, games=10):
    wins = losses = draws = 0
    for i in range(games):
        white, black = (player_a, player_b) if i % 2 == 0 else (player_b, player_a)
        result, board = play_game(white, black, random_opening_plies=4)
        a_is_white = white is player_a
        if result in ("1/2-1/2", "*"):
            draws += 1
        elif (result == "1-0") == a_is_white:
            wins += 1
        else:
            losses += 1
        mat = material_eval(board) * (1 if board.turn == chess.WHITE else -1)   # white-perspective
        print(f"game {i+1}: {result}  running: +{wins} -{losses} ={draws} plies={len(board.move_stack)}  white material={mat:+d}  ")
    return wins, losses, draws

if __name__ == "__main__":
    arena(AlphaBetaPlayer(depth=3), AlphaBetaPlayer(depth=1), games=10)
