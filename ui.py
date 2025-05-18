import gradio as gr
from game_logic import TicTacToe

def create_ui(play_turn_fn, auto_play_fn, compare_fn, model_choices):
    # Enhanced UI with names and a more polished layout
    game = TicTacToe()
    board_display = gr.HTML(value=render_board(game.board), label="Tic Tac Toe Arena 🧠🤖")
    status_text = gr.Textbox(label="Game Status", value="X's Turn")

    with gr.Row():
        player1_name = gr.Textbox(label="Player X Name", value="Alpha")
        player1 = gr.Dropdown(choices=model_choices, value=model_choices[0], label="Player X Model")
        player2_name = gr.Textbox(label="Player O Name", value="Beta")
        player2 = gr.Dropdown(choices=model_choices, value=model_choices[1], label="Player O Model")

    with gr.Row():
        play_button = gr.Button("Play Turn")
        autoplay_button = gr.Button("Auto Play Game")

    with gr.Row():
        num_games = gr.Slider(minimum=1, maximum=50, value=10, step=1, label="Compare Games Count")
        compare_btn = gr.Button("Compare Showdown")
        comparison_output = gr.Textbox(label="Model Showdown Result")

    def wrapped_play(player1_model, player2_model, name1, name2):
        result = play_turn_fn(player1_model, player2_model, game)
        return render_board(result[0]), result[1], result[2]

    def wrapped_autoplay(player1_model, player2_model):
        result = auto_play_fn(player1_model, player2_model)
        return render_board(result[0]), result[1], result[2]

    def wrapped_compare(player1_model, player2_model, count):
        return compare_fn(player1_model, player2_model, count)

    play_button.click(fn=wrapped_play, inputs=[player1, player2, player1_name, player2_name], outputs=[board_display, status_text, play_button])
    autoplay_button.click(fn=wrapped_autoplay, inputs=[player1, player2], outputs=[board_display, status_text, autoplay_button])
    compare_btn.click(fn=wrapped_compare, inputs=[player1, player2, num_games], outputs=comparison_output)

    return board_display, status_text, player1, player2, play_button, player1_name, player2_name

def render_board(board):
    cell_style = "width: 60px; height: 60px; text-align: center; font-size: 24px; border: 1px solid #333;"
    html = "<table style='border-collapse: collapse; margin: auto;'>"
    for row in board:
        html += "<tr>"
        for cell in row:
            html += f"<td style='{cell_style}'>{cell if cell else '&nbsp;'}</td>"
        html += "</tr>"
    html += "</table>"
    return html
