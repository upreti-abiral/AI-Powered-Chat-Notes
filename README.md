# ChatNotes

A simple desktop note-taking application built with Python, Tkinter, and SQLite.

## Overview

ChatNotes is a local note-taking app with a chat-style interface. Notes can be added from the input box, displayed with their timestamps, and searched using keywords.

I built this project to practise working with a graphical user interface, local databases, user input, and basic application structure in Python.

## Features

* Chat-style note interface
* Add notes with a timestamp
* Search notes by keyword
* Store notes locally using SQLite
* Display saved notes when the application starts
* Simple desktop interface using Tkinter and `ttk`

## How It Works

When a note is entered, the application:

1. Takes the user's input.
2. Saves the note and timestamp to the SQLite database.
3. Displays the note in the chat area.
4. Allows saved notes to be searched using the search bar.

The notes remain stored locally in the SQLite database, so they are available the next time the application is opened.

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
Contains the main application interface and user interaction.

**`notes_db.py`**
Handles the SQLite database and database operations.

**`README.md`**
Project documentation.

**`assets/`**
Contains optional application assets.

## Requirements

* Python 3.8 or newer
* Tkinter
* SQLite3

Tkinter and SQLite3 are included with most standard Python installations, so no external packages are required for the current version.

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/chatnotes.git
cd chatnotes
```

Run the application:

```bash
python chatnotes_app.py
```

A local SQLite database will be created for storing the notes.

## Database

The application uses SQLite for local storage.

### Notes Table

| Column      | Type    | Purpose                   |
| ----------- | ------- | ------------------------- |
| `id`        | INTEGER | Unique identifier         |
| `message`   | TEXT    | Note content              |
| `timestamp` | TEXT    | Time the note was created |
| `tag`       | TEXT    | Optional note tag         |

## Technologies

* **Python**
* **Tkinter / ttk**
* **SQLite3**

## What I Learned

This project gave me practical experience with:

* Building a desktop GUI with Tkinter
* Connecting a Python application to a database
* Creating and querying an SQLite database
* Handling user input
* Organising code across multiple Python files
* Designing a simple search function
* Managing application state

## Future Improvements

Possible future versions could include:

* AI-assisted note summarisation
* Voice input
* Text-to-speech
* Dark mode
* Improved tag organisation
* Cloud backup

These features are not part of the current version.

## Author

**Abiral Upreti**

This project is part of my ongoing work with Python and computer science.
