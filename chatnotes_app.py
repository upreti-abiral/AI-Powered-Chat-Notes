import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from notes_db import NotesDB
from openai import OpenAI

# Initialize OpenAI client (replace with your API key)
client = OpenAI(api_key="your_openai_api_key_here")

class ChatNotesApp:
    def __init__(self, root):
        self.db = NotesDB()
        self.root = root
        self.root.title("AI Chat Notes 🧠")
        self.root.geometry("650x500")
        self.root.config(bg="#222222")
        self.create_widgets()
        self.refresh_notes()

    def create_widgets(self):
        # Title
        title_label = tk.Label(
            self.root,
            text="AI Chat Notes 🧠",
            font=("Arial", 18, "bold"),
            bg="#222222",
            fg="#00ffcc"
        )
        title_label.pack(pady=10)

        # Search box
        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(self.root, textvariable=self.search_var, width=40)
        self.search_entry.pack(pady=5)
        self.search_entry.bind("<KeyRelease>", self.search_notes)

        # Notes list
        self.notes_list = tk.Listbox(
            self.root,
            width=60,
            height=10,
            bg="#333333",
            fg="white",
            selectbackground="#00ffcc"
        )
        self.notes_list.pack(pady=10)

        # Buttons
        btn_frame = tk.Frame(self.root, bg="#222222")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="➕ Add Note", command=self.add_note_ui, bg="#00ffcc").grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="🗑 Delete Note", command=self.delete_note, bg="#ff5555").grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="🤖 Summarize Note", command=self.summarize_note, bg="#ffaa00").grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="🔄 Refresh", command=self.refresh_notes, bg="#7777ff").grid(row=0, column=3, padx=5)

    def add_note_ui(self):
        title = simpledialog.askstring("Note Title", "Enter the title of your note:")
        if not title:
            return
        content = simpledialog.askstring("Note Content", "Enter the note content:")
        if not content:
            return
        self.db.add_note(title, content)
        messagebox.showinfo("Success", "Note added successfully!")
        self.refresh_notes()

    def delete_note(self):
        selected = self.notes_list.curselection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a note to delete.")
            return
        note_id = self.notes[selected[0]][0]
        self.db.delete_note(note_id)
        self.refresh_notes()

    def summarize_note(self):
        selected = self.notes_list.curselection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a note to summarize.")
            return

        note_id, title, content = self.notes[selected[0]]
        messagebox.showinfo("AI is Thinking 🤖", "Generating summary... Please wait a moment.")

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful AI that summarizes text clearly."},
                    {"role": "user", "content": f"Summarize this note:\n\n{content}"}
                ],
                max_tokens=100
            )
            summary = response.choices[0].message.content.strip()
            messagebox.showinfo("AI Summary", f"🧠 {summary}")

        except Exception as e:
            messagebox.showerror("Error", f"AI summary failed: {e}")

    def refresh_notes(self):
        self.notes = self.db.get_notes()
        self.notes_list.delete(0, tk.END)
        for note in self.notes:
            self.notes_list.insert(tk.END, f"{note[1]}")

    def search_notes(self, event=None):
        keyword = self.search_var.get()
        if keyword.strip() == "":
            self.refresh_notes()
        else:
            results = self.db.search_notes(keyword)
            self.notes_list.delete(0, tk.END)
            for note in results:
                self.notes_list.insert(tk.END, f"{note[1]}")
            self.notes = results


if __name__ == "__main__":
    root = tk.Tk()
    app = ChatNotesApp(root)
    root.mainloop()
