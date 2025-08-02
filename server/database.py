"""
Database setup and management for Celebrity Voice Swapper
SQLite database implementation to replace dictionary-based storage
"""

import sqlite3
import json
import os
from typing import List, Dict, Optional, Any
from contextlib import contextmanager

DATABASE_PATH = "celebrities.db"

class CelebrityDatabase:
    def __init__(self, db_path: str = DATABASE_PATH):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialize the database with required tables"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            # Create celebrities table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS celebrities (
                    id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    image TEXT,
                    bio TEXT,
                    voice_sample TEXT,
                    languages TEXT,  -- JSON array
                    popularity INTEGER,
                    debut_year INTEGER,
                    notable_films TEXT,  -- JSON array
                    voice_characteristics TEXT,  -- JSON array
                    category TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Create categories table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS categories (
                    id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    description TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Create conversion_history table for future use
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS conversion_history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    celebrity_id TEXT,
                    original_filename TEXT,
                    converted_filename TEXT,
                    conversion_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    status TEXT DEFAULT 'completed',
                    FOREIGN KEY (celebrity_id) REFERENCES celebrities (id)
                )
            ''')
            
            conn.commit()
    
    @contextmanager
    def get_connection(self):
        """Context manager for database connections"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  # Enable dict-like access to rows
        try:
            yield conn
        finally:
            conn.close()
    
    def insert_celebrity(self, celebrity_data: Dict[str, Any]) -> bool:
        """Insert a new celebrity into the database"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                
                cursor.execute('''
                    INSERT OR REPLACE INTO celebrities 
                    (id, name, image, bio, voice_sample, languages, popularity, 
                     debut_year, notable_films, voice_characteristics, category)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    celebrity_data['id'],
                    celebrity_data['name'],
                    celebrity_data.get('image', ''),
                    celebrity_data.get('bio', ''),
                    celebrity_data.get('voice_sample', ''),
                    json.dumps(celebrity_data.get('languages', [])),
                    celebrity_data.get('popularity', 0),
                    celebrity_data.get('debut_year', 0),
                    json.dumps(celebrity_data.get('notable_films', [])),
                    json.dumps(celebrity_data.get('voice_characteristics', [])),
                    celebrity_data['category']
                ))
                
                conn.commit()
                return True
        except Exception as e:
            print(f"Error inserting celebrity: {e}")
            return False
    
    def get_all_celebrities(self) -> List[Dict[str, Any]]:
        """Get all celebrities from the database"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM celebrities ORDER BY popularity DESC')
                rows = cursor.fetchall()
                
                celebrities = []
                for row in rows:
                    celebrity = dict(row)
                    # Parse JSON fields
                    celebrity['languages'] = json.loads(celebrity['languages'])
                    celebrity['notable_films'] = json.loads(celebrity['notable_films'])
                    celebrity['voice_characteristics'] = json.loads(celebrity['voice_characteristics'])
                    celebrities.append(celebrity)
                
                return celebrities
        except Exception as e:
            print(f"Error fetching all celebrities: {e}")
            return []
    
    def get_celebrities_by_category(self, category: str) -> List[Dict[str, Any]]:
        """Get celebrities by category"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    'SELECT * FROM celebrities WHERE category = ? ORDER BY popularity DESC',
                    (category,)
                )
                rows = cursor.fetchall()
                
                celebrities = []
                for row in rows:
                    celebrity = dict(row)
                    # Parse JSON fields
                    celebrity['languages'] = json.loads(celebrity['languages'])
                    celebrity['notable_films'] = json.loads(celebrity['notable_films'])
                    celebrity['voice_characteristics'] = json.loads(celebrity['voice_characteristics'])
                    celebrities.append(celebrity)
                
                return celebrities
        except Exception as e:
            print(f"Error fetching celebrities by category: {e}")
            return []
    
    def get_celebrity_by_id(self, celebrity_id: str) -> Optional[Dict[str, Any]]:
        """Get a specific celebrity by ID"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM celebrities WHERE id = ?', (celebrity_id,))
                row = cursor.fetchone()
                
                if row:
                    celebrity = dict(row)
                    # Parse JSON fields
                    celebrity['languages'] = json.loads(celebrity['languages'])
                    celebrity['notable_films'] = json.loads(celebrity['notable_films'])
                    celebrity['voice_characteristics'] = json.loads(celebrity['voice_characteristics'])
                    return celebrity
                
                return None
        except Exception as e:
            print(f"Error fetching celebrity by ID: {e}")
            return None
    
    def get_categories(self) -> List[str]:
        """Get all available categories"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT DISTINCT category FROM celebrities ORDER BY category')
                rows = cursor.fetchall()
                return [row['category'] for row in rows]
        except Exception as e:
            print(f"Error fetching categories: {e}")
            return []
    
    def search_celebrities(self, query: str) -> List[Dict[str, Any]]:
        """Search celebrities by name or characteristics"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                search_query = f"%{query.lower()}%"
                
                cursor.execute('''
                    SELECT * FROM celebrities 
                    WHERE LOWER(name) LIKE ? 
                       OR LOWER(bio) LIKE ? 
                       OR LOWER(voice_characteristics) LIKE ?
                    ORDER BY popularity DESC
                ''', (search_query, search_query, search_query))
                
                rows = cursor.fetchall()
                
                celebrities = []
                for row in rows:
                    celebrity = dict(row)
                    # Parse JSON fields
                    celebrity['languages'] = json.loads(celebrity['languages'])
                    celebrity['notable_films'] = json.loads(celebrity['notable_films'])
                    celebrity['voice_characteristics'] = json.loads(celebrity['voice_characteristics'])
                    celebrities.append(celebrity)
                
                return celebrities
        except Exception as e:
            print(f"Error searching celebrities: {e}")
            return []
    
    def add_conversion_history(self, celebrity_id: str, original_filename: str, 
                             converted_filename: str, status: str = 'completed') -> bool:
        """Add a conversion record to history"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO conversion_history 
                    (celebrity_id, original_filename, converted_filename, status)
                    VALUES (?, ?, ?, ?)
                ''', (celebrity_id, original_filename, converted_filename, status))
                
                conn.commit()
                return True
        except Exception as e:
            print(f"Error adding conversion history: {e}")
            return False
    
    def get_conversion_history(self, limit: int = 50) -> List[Dict[str, Any]]:
        """Get conversion history"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT ch.*, c.name as celebrity_name 
                    FROM conversion_history ch
                    LEFT JOIN celebrities c ON ch.celebrity_id = c.id
                    ORDER BY ch.conversion_time DESC
                    LIMIT ?
                ''', (limit,))
                
                rows = cursor.fetchall()
                return [dict(row) for row in rows]
        except Exception as e:
            print(f"Error fetching conversion history: {e}")
            return []

# Global database instance
db = CelebrityDatabase()
