import os
import openai
import random
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

available_models = [
    "gpt-3.5-turbo",
    "gpt-3.5-turbo-16k",
    "gpt-4",
    "gpt-4-32k",
    "gpt-4-turbo"
]

def get_llm_move(model, board, player):
    prompt = f"You are playing tic tac toe as {player}. Board state is:\n{board}\nGive your move as row,col"
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
        )
        content = response["choices"][0]["message"]["content"]
        row, col = map(int, content.strip().split(","))
        return row, col
    except:
        return random.choice([(i, j) for i in range(3) for j in range(3) if board[i][j] == ""])
