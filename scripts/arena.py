import chess
from engine.game import play_game
from engine.players import RandomPlayer
from engine.search import AlphaBetaPlayer

def arena(player_a, player_b, games=10):
    wins = losses = draws = 0
    for i in range(games):
        white, black = (player_a, player_b) if i % 2 == 0 else (player_b, player_a)
        result, _ = play_game(white, black)
        a_is_white = white is player_a
        if result in ("1/2-1/2", "*"):
            draws += 1
        elif (result == "1-0") == a_is_white:
            wins += 1
        else:
            losses += 1
        print(f"game {i+1}: {result}   running: +{wins} -{losses} ={draws}")
    return wins, losses, draws

if __name__ == "__main__":
    arena(AlphaBetaPlayer(depth=3), AlphaBetaPlayer(depth=1), games=10)
