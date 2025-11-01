"""
Module sqlite_manager.py
"""
import sqlite3
from models.island import Island
from models.tile import Tile
from typing import Optional

class SQLiteManager:
    """
    Manager to manage the SQLite database for the island and tiles.
    """
    def __init__(self, db_path: str = "islandgen.db"):
        self.db_path = db_path
        self.conn: Optional[sqlite3.Connection] = None

    def connect(self):
        """Connects the database and creates tables if necessary."""
        self.conn = sqlite3.connect(self.db_path)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        # Island table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS island (
            id INTEGER PRIMARY KEY,
            name TEXT,
            width INTEGER,
            height INTEGER,
            population INTEGER,
            wealth TEXT,
            crime TEXT,
            climate TEXT,
            biomes TEXT,
            seed INTEGER,
            created_at TEXT
        )
        """)
        # Tile table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tile (
            id INTEGER PRIMARY KEY,
            island_id INTEGER,
            x INTEGER,
            y INTEGER,
            biome TEXT,
            special TEXT,
            description TEXT,
            FOREIGN KEY (island_id) REFERENCES island(id)
        )
        """)
        # TileImage table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tile_image (
            id INTEGER PRIMARY KEY,
            tile_id INTEGER,
            path TEXT,
            FOREIGN KEY (tile_id) REFERENCES tile(id)
        )
        """)
        self.conn.commit()

    def close(self):
        if self.conn:
            self.conn.close()
