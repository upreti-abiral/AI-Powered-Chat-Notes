import os
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

from notes_db import NotesDB
from openai import OpenAI


class ChatNotesApp:
    def __init__(self, root):
        self.db = NotesDB()
        self.root = root

        api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=api_key) if api_key else None

        self.root.title("ChatNotes")
        self.root.geometry("650x500")
        self.root.config(bg="#222222")

        self.create_widgets()
        self.refresh_notes()

    def create_widgets(self):
        title_label = tk.Label(
            self.root,
            text="ChatNotes",
            font=("Arial", 18, "bold"),
            bg="#222222",
            fg="#00ffcc"
        )
        title_label.pack(pady=10)

        self.search_var = tk.StringVar()

        self.search_entry = ttk.Entry(
            self.root,
            textvariable=self.search_var,
            width=40
        )
        self.search_entry.pack(pady=5)
        self.search_entry.bind("<KeyRelease>", self.search_notes)

        self.notes_list = tk.Listbox(
            self.root,
            width=60,
            height=10,
            bg="#333333",
            fg="white",
            selectbackground="#00ffcc"
        )
        self.notes_list.pack(pady=10)

        button_frame = tk.Frame(self.root, bg="#222222")
        button_frame.pack(pady=10)

        tk.Button(
            button_frame,
            text="Add Note",
            command=self.add_note_ui,
            bg="#00ffcc"
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            button_frame,
            text="Delete Note",
            command=self.delete_note,
            bg="#ff5555"
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            button_frame,
            text="Summarize Note",
            command=self.summarize_note,
            bg="#ffaa00"
        ).grid(row=0, column=2, padx=5)

        tk.Button(
            button_frame,
            text="Refresh",
            command=self.refresh_notes,
            bg="#7777ff"
        ).grid(row=0, column=3, padx=5)

    def add_note_ui(self):
        title = simpledialog.askstring(
            "Note Title",
            "Enter the title of your note:"
        )

        if not title:
            return

        content = simpledialog.askstring(
            "Note Content",
            "Enter the note content:"
        )

        if not content:
            return

        self.db.add_note(title, content)
        self.refresh_notes()

    def delete_note(self):
        selected = self.notes_list.curselection()

        if not selected:
            messagebox.showwarning(
                "Warning",
                "Please select a note to delete."
            )
            return

        note_id = self.notes[selected[0]][0]
        self.db.delete_note(note_id)
        self.refresh_notes()

    def summarize_note(self):
        selected = self.notes_list.curselection()

        if not selected:
            messagebox.showwarning(
                "Warning",
                "Please select a note to summarize."
            )
            return

        if self.client is None:
            messagebox.showerror(
                "AI Unavailable",
                "OpenAI API key not found. Set the OPENAI_API_KEY environment variable."
            )
            return

        note_id, title, content, timestamp = self.notes[selected[0]]

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": "Summarize the user's note clearly and briefly."
                    },
                    {
                        "role": "user",
                        "content": content
                    }
                ],
                max_tokens=100
            )

            summary = response.choices[0].message.content.strip()

            messagebox.showinfo(
                "AI Summary",
                summary
            )

        except Exception as error:
            messagebox.showerror(
                "Error",
                "Could not generate the summary.\n\n"
                + str(error)
            )

    def refresh_notes(self):
        self.notes = self.db.get_notes()

        self.notes_list.delete(0, tk.END)

        for note in self.notes:
            self.notes_list.insert(
                tk.END,
                note[1] + "  |  " + note[3]
            )

    def search_notes(self, event=None):
        keyword = self.search_var.get().strip()

        if keyword == "":
            self.refresh_notes()
            return

        self.notes = self.db.search_notes(keyword)

        self.notes_list.delete(0, tk.END)

        for note in self.notes:
            self.notes_list.insert(
                tk.END,
                note[1] + "  |  " + note[3]
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = ChatNotesApp(root)
    root.mainloop()
