# 🤖 Tic Tac Toe LLM Showdown

Welcome to **Tic Tac Toe Arena**, a web-based showdown between two Large Language Models (LLMs) playing Tic Tac Toe against each other!
Built using **Gradio**, **OpenAI APIs**, and Python 🐍.

---

## 🎮 Features

* Play Tic Tac Toe where **two OpenAI LLMs compete**
* Choose any two models (e.g., `gpt-3.5-turbo` vs `gpt-4`)
* Visual board with X/O tokens
* Option to:

  * Step through one turn at a time
  * Auto-play an entire game
  * Simulate multiple games and compare which model wins more

---

## 📸 Demo Screenshot

![App Screenshot](https://user-images.githubusercontent.com/your_username/screenshot-placeholder.png)

---

## ✨ Try It Out

To run locally:

### 1. 🔑 Set up your `.env`

Create a `.env` file (not committed) with:

```
OPENAI_API_KEY=your_openai_api_key_here
```

### 2. 🛆 Install dependencies

```bash
pip install -r requirements.txt
```

### 3. ▶️ Run the app

```bash
python app.py
```

Then open your browser to: [http://localhost:7860](http://localhost:7860)

---

## 🗂️ Project Structure

```
tic_tac_toe_llms/
├── app.py             # Main Gradio interface
├── game_logic.py      # Core game rules & logic
├── llm_interface.py   # LLM API calls and prompting
├── ui.py              # UI layout using Gradio Blocks
├── requirements.txt   # Python dependencies
├── .env               # Your OpenAI API key (NOT COMMITTED)
├── .gitignore         # Ignore .env and system files
```

---

## 🤖 Supported Models

You can choose from any available OpenAI models like:

* `gpt-3.5-turbo`
* `gpt-3.5-turbo-16k`
* `gpt-4`
* `gpt-4-32k`
* `gpt-4-turbo`

---

## 📊 Model Showdown Mode

Compare two models by running 10+ auto-played games.
Results like:

```
Out of 10 games:
gpt-4 (X) won 6 times
gpt-3.5-turbo (O) won 3 times
Draws: 1
```

---

## ☁️ Deploy on Hugging Face Spaces

1. [Create a new Space](https://huggingface.co/spaces)
2. Choose **Gradio** SDK
3. Add the `OPENAI_API_KEY` as an Environment Variable
4. Push this code repo (excluding `.env`) using `git`

---

## 📃 License

MIT License © 2024 Pradyumna Elavarthi

---

## 🙋‍♀️ Acknowledgments

Built with ❤️ using:

* [OpenAI API](https://platform.openai.com/docs)
* [Gradio](https://gradio.app)
