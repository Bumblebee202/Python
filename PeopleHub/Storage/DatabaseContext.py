import sqlite3
import os
import sys

class DatabaseContext:
    def __init__(self):
        exeDirectory = os.path.dirname(sys.executable)
        self.dbPath = os.path.join(exeDirectory, "contacts.db")
        self.connection = None


    def __enter__(self):
        self.InitDatabase()
        self.connection = sqlite3.connect(self.dbPath)
        self.connection.row_factory = sqlite3.Row
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()


    def InitDatabase(self):
        if os.path.exists(self.dbPath):
            return

        connection = sqlite3.connect(self.dbPath)
        cursor = connection.cursor()

        cursor.execute("""
        create table if not exists Contacts (
            Id integer not null primary key autoincrement,
            Name text not null,
            Phone text not null unique,
            Email text not null unique,
            Address text not null,
            Notes text
        )
        """)

        connection.commit()