🧠 ChatNotes — AI-Powered Chat Notes App
✨ Overview

ChatNotes is a modern, chat-style notebook app built with Python and Tkinter.
It lets you write notes like you’re chatting, tag or search them instantly, and later upgrade to add AI-powered summarization, voice input, or cloud sync.

It’s lightweight, aesthetic, and perfect for students, creators, or anyone who wants a cleaner note experience.

🚀 Features

✅ Minimal & modern chat-style interface
✅ Instant note saving with timestamp
✅ Search your notes by keywords or tags
✅ Simple, local SQLite database storage
✅ Clean UI built using Tkinter + ttk

Upcoming Upgrades (Planned):
🪄 AI note summarizer (OpenAI API)
🎤 Voice input (speech-to-text)
🔊 Text-to-speech reader
🌗 Dark mode toggle
🔖 Tag-based organization
☁️ Cloud sync with Google Drive / Firebase

🧩 Project Structure
chatnotes/
│
├── chatnotes_app.py      # Main Tkinter UI (chat-like)
├── notes_db.py           # Handles database and queries
├── README.md             # Project documentation
└── assets/
    └── icon.png          # (Optional) App icon

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/chatnotes.git
cd chatnotes

2️⃣ Install Python Requirements

You don’t need any external libraries (Tkinter and SQLite come built-in with Python).
Just ensure you have Python 3.8+ installed.

3️⃣ Run the App
python chatnotes_app.py

💬 How It Works

Type a note in the input bar and press Enter or click Add Note.

Your note appears instantly in the chat area with a timestamp.

Use the search bar to filter through notes in real time.

All notes are stored locally in chatnotes.db (SQLite).

🖼️ Screenshot (example layout)

(Add this once you run the app and take a screenshot)

🧠 Chat Notes 💬

[ Chat-like interface showing timestamped notes ]

🧠 Future Upgrades (Phase 2 & 3)
Feature	Description	Library
🪄 AI Summarizer	Summarize notes or entire days	openai
🎤 Voice Input	Convert speech to note text	speech_recognition
🔊 Text-to-Speech	Read notes aloud	pyttsx3
🌗 Dark Mode	Toggle themes	ttkbootstrap
☁️ Cloud Sync	Backup to Google Drive	pydrive / firebase-admin
📦 Database Schema
Column	Type	Description
id	INTEGER	Primary Key
message	TEXT	The note content
timestamp	TEXT	When the note was added
tag	TEXT	(Optional) topic tag
🧰 Tech Stack

Python 3.8+

Tkinter (for UI)

SQLite3 (for storage)

👨‍💻 Author

Developed by: [Abiral Upreti]
📧 Email: abiralzone@gmail.com

🌐 GitHub: Abiral Upreti

🪪 License

This project is open-source under the MIT License
.
Feel free to fork and enhance — credits appreciated 💙
