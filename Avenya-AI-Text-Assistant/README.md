🤖 Avenya — AI Text Assistant

Avenya is a Python-based terminal AI text assistant designed to combine simple command-based actions with AI-powered responses.

It can handle predefined commands, open commonly used websites, provide information about itself, and send user questions to an AI service through the Groq API.

✨ Features

- 🤖 AI-powered text responses
- 💻 Terminal-based interface
- ⌨️ Typing-effect introduction
- 🧭 Built-in command handling
- 🌐 Opens Google, YouTube, ChatGPT, and GitHub
- ℹ️ Includes Help and About Avenya commands
- 🔐 API key loaded securely through an environment variable
- ⏱️ API request timeout and connection error handling
- 🐍 Built with Python

🎮 Available Commands

Help
About Avenya
Avenya open Google
Avenya open YouTube
Avenya open ChatGPT
Avenya open GitHub
Exit

Any input that is not a recognized built-in command is handled as an AI request.

🛠️ Technologies Used

- Python
- "requests"
- "python-dotenv"
- "webbrowser"
- Groq API
- Environment variables

📁 Project Structure

Avenya-AI-Text-Assistant/
│
├── Avenya.py
├── .gitignore
└── README.md

«The ".env" file is intentionally excluded from this repository because it contains the private API key.»

⚙️ Setup

1. Clone or download the repository

Download the project files to your device.

2. Install dependencies

pip install requests python-dotenv

3. Create the ".env" file

Create a file named:

.env

Add your own Groq API key using the environment variable:

GROQ_API_KEY=your_api_key_here

Never publish your real API key on GitHub.

4. Run Avenya

Run the Python source file:

python Avenya.py

🔐 Security Note

Avenya loads the Groq API key from an environment variable instead of placing the secret directly inside the Python source code.

The ".env" file is excluded using ".gitignore" and should never be committed to the repository.

🎯 Project Purpose

Avenya was created as a hands-on Python project to practice:

- Functions
- Conditional logic
- Loops
- Exception handling
- API requests
- Environment variables
- Command validation
- JSON response handling
- Basic automation with "webbrowser"

👨‍💻 Creator

Anshul — ANSHUL-CODES

Created: August 8, 2026

Language: Python 🐍

Status: Online 🟢

---

Avenya is a learning project built with Python and API integration.
