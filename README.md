# ChatNotes

A desktop note-taking application built with Python, Tkinter, SQLite, and the OpenAI API.

## Overview

ChatNotes is a local note-taking application with a simple desktop interface. Users can create, view, search, and delete notes, as well as generate a short AI summary of a selected note.

The project combines a graphical user interface, local database storage, and an external AI API in one Python application.

## Features

* Create notes with a title and content
* Store notes locally using SQLite
* Display saved notes with timestamps
* Search notes by title or content
* Delete notes
* Generate AI summaries of selected notes
* Simple desktop interface built with Tkinter

## How It Works

When a note is created, ChatNotes stores its title, content, and timestamp in a local SQLite database.

The application can then:

1. Load saved notes from the database.
2. Display them in the interface.
3. Search notes using a keyword.
4. Delete selected notes.
5. Send the selected note to the OpenAI API when an AI summary is requested.
6. Display the generated summary to the user.

The notes database remains local to the computer. Only the note content used for summarisation is sent to the OpenAI API when that feature is used.

## Project Structure

```text
ChatNotes/
│
├── chatnotes_app.py
├── notes_db.py
├── README.md
└── assets/
    └── icon.png
```

### Files

**`chatnotes_app.py`**
Contains the graphical interface, user interaction, note management, search, and AI summarisation.

**`notes_db.py`**
Handles SQLite database creation, storing notes, retrieving notes, deleting notes, and searching.

**`README.md`**
Project documentation.

**`assets/`**
Contains optional application assets.

## Technologies

* **Python**
* **Tkinter / ttk** for the graphical interface
* **SQLite3** for local data storage
* **OpenAI API** for note summarisation

## Requirements

* Python 3.8+
* OpenAI Python library
* An OpenAI API key

Tkinter and SQLite3 are included with most standard Python installations.

Install the OpenAI library:

```bash
pip install openai
```

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/chatnotes.git
cd chatnotes
```

Install the required package:

```bash
pip install openai
```

## API Key Setup

The application reads the OpenAI API key from an environment variable.

### Windows PowerShell

```powershell
$env:OPENAI_API_KEY="your_api_key_here"
```

### macOS / Linux

```bash
export OPENAI_API_KEY="your_api_key_here"
```

Do **not** place your API key directly inside `chatnotes_app.py` or commit it to GitHub.

## Run the Application

```bash
python chatnotes_app.py
```

A local SQLite database will be created automatically when the application starts.

## Database

ChatNotes uses SQLite for local note storage.

### Notes Table

| Column      | Type    | Description               |
| ----------- | ------- | ------------------------- |
| `id`        | INTEGER | Unique note identifier    |
| `title`     | TEXT    | Note title                |
| `content`   | TEXT    | Note content              |
| `timestamp` | TEXT    | Time the note was created |

## AI Summarisation

The **Summarize Note** feature uses the OpenAI API to generate a short summary of the selected note.

If an API key is not configured, the rest of the application can still be used for creating, searching, viewing, and deleting notes. AI summarisation simply remains unavailable.

## What I Learned

This project gave me practical experience with several areas of Python development:

* Building a desktop GUI with Tkinter
* Organising an application across multiple Python files
* Creating and querying an SQLite database
* Handling user input and application events
* Searching and managing stored data
* Working with an external API
* Handling API errors and missing configuration
* Keeping API credentials outside the source code

## Future Improvements

Possible future versions could include:

* Better note editing
* Note categories or tags
* Voice input
* Text-to-speech
* Dark mode
* Improved AI features
* Cloud backup

These features are not part of the current version.

## Author

**Abiral Upreti**

A Python project focused on learning application development, databases, and AI integration.
