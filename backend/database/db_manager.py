# backend/database/db_manager.py

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "embeddings.db")

def create_tables():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS embeddings (
                id TEXT PRIMARY KEY,
                type TEXT NOT NULL,
                embedding TEXT NOT NULL
            )
        ''')
        conn.commit()

def get_embedding_from_db(entity_id: str, entity_type: str):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT embedding FROM embeddings WHERE id = ? AND type = ?
        ''', (entity_id, entity_type))
        result = cursor.fetchone()
        if result:
            return [float(x) for x in result[0].split(',')]
        return None

def save_embedding_to_db(entity_id: str, entity_type: str, embedding: list):
    embedding_str = ','.join(map(str, embedding))
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO embeddings (id, type, embedding)
            VALUES (?, ?, ?)
        ''', (entity_id, entity_type, embedding_str))
        conn.commit()
