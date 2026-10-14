from engine.players import RandomPlayer
from engine.game import play_game

result, board = play_game(RandomPlayer(), RandomPlayer(), verbose=True)
print("Result:", result)
print("Moves played:", len(board.move_stack))
