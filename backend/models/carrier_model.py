import json
from database.db import connect_db

class CareerModel:
    def __init__(self):
        pass

    def _get_db(self):
        from database.db import connect_db
        return connect_db()

    def get_all_careers(self):
        db = self._get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM careers')
        rows = cursor.fetchall()
        db.close()
        careers = []
        for row in rows:
            careers.append({
                'id': row[0],
                'title': row[1],
                'category': row[2],
                'description': row[3],
                'skills': json.loads(row[4]) if row[4] else [],
                'education': row[5],
                'experience': row[6],
                'salary_range': row[7],
                'job_growth': row[8]
            })
        return careers

    def get_career_by_id(self, career_id):
        db = self._get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM careers WHERE id = ?', (career_id,))
        row = cursor.fetchone()
        db.close()
        if row:
            return {
                'id': row[0],
                'title': row[1],
                'category': row[2],
                'description': row[3],
                'skills': json.loads(row[4]) if row[4] else [],
                'education': row[5],
                'experience': row[6],
                'salary_range': row[7],
                'job_growth': row[8]
            }
        return None

    def get_career_by_name(self, name):
        db = self._get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM careers WHERE title LIKE ?', ('%' + name + '%',))
        row = cursor.fetchone()
        db.close()
        if row:
            return {
                'id': row[0],
                'title': row[1],
                'category': row[2],
                'description': row[3],
                'skills': json.loads(row[4]) if row[4] else [],
                'education': row[5],
                'experience': row[6],
                'salary_range': row[7],
                'job_growth': row[8]
            }
        return None

    def get_careers_by_skill(self, skill):
        all_careers = self.get_all_careers()
        matching_careers = []
        for career in all_careers:
            if skill.lower() in [s.lower() for s in career.get('skills', [])]:
                matching_careers.append(career)
        return matching_careers

    def get_careers_by_category(self, category):
        db = self._get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM careers WHERE category = ?', (category,))
        rows = cursor.fetchall()
        db.close()
        careers = []
        for row in rows:
            careers.append({
                'id': row[0],
                'title': row[1],
                'category': row[2],
                'description': row[3],
                'skills': json.loads(row[4]) if row[4] else [],
                'education': row[5],
                'experience': row[6],
                'salary_range': row[7],
                'job_growth': row[8]
            })
        return careers
