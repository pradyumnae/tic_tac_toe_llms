import gradio as gr
from game_logic import TicTacToe
from ui import create_ui
from llm_interface import get_llm_move, available_models

# Initialize Game
def play_turn(player_model_1, player_model_2, game):
    if game.is_game_over():
        return game.board, f"Game Over! Winner: {game.winner}", gr.update(interactive=False)

    current_model = player_model_1 if game.current_player == "X" else player_model_2
    move = get_llm_move(current_model, game.board, game.current_player)
    game.make_move(*move)
    status = f"{game.current_player}'s Turn" if not game.is_game_over() else f"Game Over! Winner: {game.winner}"
    return game.board, status, gr.update()

def auto_play(player_model_1, player_model_2):
    game = TicTacToe()
    while not game.is_game_over():
        current_model = player_model_1 if game.current_player == "X" else player_model_2
        move = get_llm_move(current_model, game.board, game.current_player)
        game.make_move(*move)
    return game.board, f"Game Over! Winner: {game.winner}", gr.update(interactive=False)

def compare_models(player_model_1, player_model_2, num_games):
    x_wins = 0
    o_wins = 0
    draws = 0
    for _ in range(num_games):
        game = TicTacToe()
        while not game.is_game_over():
            current_model = player_model_1 if game.current_player == "X" else player_model_2
            move = get_llm_move(current_model, game.board, game.current_player)
            game.make_move(*move)
        if game.winner == "X":
            x_wins += 1
        elif game.winner == "O":
            o_wins += 1
        else:
            draws += 1
    summary = f"Out of {num_games} games:\n{player_model_1} (X) won {x_wins} times\n{player_model_2} (O) won {o_wins} times\nDraws: {draws}"
    return summary

with gr.Blocks() as demo:
    gr.HTML("""
<div style='text-align: center; font-family: Trebuchet MS, sans-serif;'>
    <h1 style='font-size: 36px; color: #3b82f6;'>🧠🤖 <span style='color:#ef4444;'>Tic Tac Toe Arena</span></h1>
    <p style='font-size: 20px; color: #10b981;'>Battle of Language Models — Who plays smarter?</p>
</div>
""")
    board_display, status_text, player1, player2, play_button, player1_name, player2_name = create_ui(
        play_turn, auto_play, compare_models, available_models
    )

demo.launch()
