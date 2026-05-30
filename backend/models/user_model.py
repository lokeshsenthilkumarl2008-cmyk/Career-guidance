
import sqlite3
import json
from database.db import connect_db

class UserModel:
    def __init__(self):
        pass  # Don't store connection

    def _get_db(self):
        return connect_db()

    def create_user(self, name, skills, interests, education):
        db = self._get_db()
        cursor = db.cursor()
        cursor.execute('''
            INSERT INTO users (name, skills, interests, education, progress)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, json.dumps(skills), json.dumps(interests), education, json.dumps({})))
        db.commit()
        db.close()
        return cursor.lastrowid

    def get_user(self, user_id):
        db = self._get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        row = cursor.fetchone()
        db.close()
        if row:
            return {
                'id': row[0],
                'name': row[1],
                'skills': json.loads(row[2]),
                'interests': json.loads(row[3]),
                'education': row[4],
                'progress': json.loads(row[5])
            }
        return None

    def update_user(self, user_id, data):
        db = self._get_db()
        cursor = db.cursor()
        updates = []
        params = []
        if 'name' in data:
            updates.append('name = ?')
            params.append(data['name'])
        if 'skills' in data:
            updates.append('skills = ?')
            params.append(json.dumps(data['skills']))
        if 'interests' in data:
            updates.append('interests = ?')
            params.append(json.dumps(data['interests']))
        if 'education' in data:
            updates.append('education = ?')
            params.append(data['education'])
        if 'progress' in data:
            updates.append('progress = ?')
            params.append(json.dumps(data['progress']))
        params.append(user_id)
        cursor.execute(f'UPDATE users SET {", ".join(updates)} WHERE id = ?', params)
        db.commit()
        db.close()
        return cursor.rowcount > 0

    def get_all_users(self):
        db = self._get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM users')
        rows = cursor.fetchall()
        db.close()
        users = []
        for row in rows:
            users.append({
                'id': row[0],
                'name': row[1],
                'skills': json.loads(row[2]),
                'interests': json.loads(row[3]),
                'education': row[4],
                'progress': json.loads(row[5])
            })
        return users
