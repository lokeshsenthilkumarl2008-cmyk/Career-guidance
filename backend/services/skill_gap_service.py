# Compare user skills with required career skills
# Input: selected career + user skills
# Output: missing skills (skill gap)

from models.carrier_model import CareerModel

class SkillGapService:
    def __init__(self):
        self.career_model = CareerModel()

    def analyze_skill_gap(self, career_name, user_skills):
        career = self.career_model.get_career_by_name(career_name)
        if not career:
            return {'error': 'Career not found'}

        required_skills = set(career.get('skills', []))
        user_skills_set = set(user_skills)

        missing_skills = list(required_skills - user_skills_set)
        matched_skills = list(required_skills.intersection(user_skills_set))

        return {
            'career': career_name,
            'required_skills': list(required_skills),
            'user_skills': list(user_skills_set),
            'missing_skills': missing_skills,
            'matched_skills': matched_skills,
            'gap_percentage': (len(missing_skills) / len(required_skills)) * 100 if required_skills else 0
        }