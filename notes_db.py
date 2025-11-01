import sqlite3

class NotesDB:
    def __init__(self, db_name="chatnotes.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_note(self, title, content):
        query = "INSERT INTO notes (title, content) VALUES (?, ?)"
        self.conn.execute(query, (title, content))
        self.conn.commit()

    def get_notes(self):
        query = "SELECT id, title, content FROM notes"
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def delete_note(self, note_id):
        query = "DELETE FROM notes WHERE id = ?"
        self.conn.execute(query, (note_id,))
        self.conn.commit()

    def search_notes(self, keyword):
        query = "SELECT id, title, content FROM notes WHERE title LIKE ? OR content LIKE ?"
        cursor = self.conn.execute(query, (f"%{keyword}%", f"%{keyword}%"))
        return cursor.fetchall()

    def close(self):
        self.conn.close()
