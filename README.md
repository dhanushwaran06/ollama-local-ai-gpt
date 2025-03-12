# Ollama Local AI GPT

A modern local AI chat application using **Ollama**, **Flask**, and **MySQL**. This project allows you to interact with a local AI model, store conversations in a database, and enjoy a sleek user interface.
---
## Screenshots

### Screenshot 1
![Screenshot 1](https://raw.githubusercontent.com/dhanushwaran06/ollama-local-ai-gpt/main/sample_screenshot_1%20.png)


### Screenshot 2
![Screenshot 1](https://raw.githubusercontent.com/dhanushwaran06/ollama-local-ai-gpt/main/sample_screenshot_2%20.png)

## Features

- **Local AI Interaction**: Chat with a local AI model using Ollama.
- **Modern UI**: Sleek and responsive user interface built with Bootstrap 5.
- **Conversation Storage**: All chats are stored in a MySQL database for persistence.
- **Typing Effect**: Simulates a typing effect for the bot's responses.
- **Easy Setup**: Simple installation and configuration.

---

## Technologies Used

- **Python**: Backend logic and API handling.
- **Flask**: Web framework for serving the application.
- **Ollama**: Local AI model interaction.
- **MySQL**: Database for storing conversations.
- **Bootstrap 5**: Modern and responsive UI design.
- **jQuery**: Frontend interactivity.

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/LocalAIChat.git
   cd LocalAIChat
   ```

2. **Set up a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up MySQL**:
   - Create a database named `ollama_chat`.
   - Update the `db_config` in `app.py` with your MySQL credentials.

5. **Run the application**:
   ```bash
   python app.py
   ```

6. **Access the application**:
   Open your browser and go to `http://127.0.0.1:5001`.

---

## Usage

1. Type your message in the input box and press **Send**.
2. The bot will respond with a typing effect.
3. All conversations are stored in the MySQL database.

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.

---

## Acknowledgments

- [Ollama](https://ollama.ai) for the local AI model.
- [Bootstrap](https://getbootstrap.com) for the UI framework.
- [Flask](https://flask.palletsprojects.com) for the web framework.
