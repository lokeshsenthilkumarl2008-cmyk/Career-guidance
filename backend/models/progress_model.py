
import json
from database.db import connect_db

class ProgressModel:
    def __init__(self):
        pass

    def _get_db(self):
        from database.db import connect_db
        return connect_db()

    def save_progress(self, user_id, completed_skills, current_step, progress_percentage, roadmap=None):
        db = self._get_db()
        cursor = db.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO progress (user_id, completed_skills, current_step, progress_percentage, roadmap)
            VALUES (?, ?, ?, ?, ?)
        ''', (user_id, json.dumps(completed_skills), current_step, progress_percentage, json.dumps(roadmap) if roadmap else None))
        db.commit()
        db.close()
        return True

    def get_progress(self, user_id):
        db = self._get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM progress WHERE user_id = ?', (user_id,))
        row = cursor.fetchone()
        db.close()
        if row:
            return {
                'user_id': row[0],
                'completed_skills': json.loads(row[1]) if row[1] else [],
                'current_step': row[2],
                'progress_percentage': row[3],
                'roadmap': json.loads(row[4]) if row[4] else None
            }
        return None
