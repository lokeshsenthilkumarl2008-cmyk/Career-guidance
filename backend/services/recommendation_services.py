# Build recommendation engine
# Input: user skills, interests
# Load career data from careers.json
# Match user profile with careers
# Calculate score for each career
# Return top 3–5 careers with match percentage and explanation

from models.carrier_model import CareerModel
import json

class RecommendationService:
    def __init__(self):
        self.career_model = CareerModel()

    def recommend_careers(self, user_skills, user_interests, user_education):
        careers = self.career_model.get_all_careers()
        recommendations = []

        for career in careers:
            score = self._calculate_match_score(user_skills, user_interests, user_education, career)
            explanation = self._generate_explanation(score, career)
            recommendations.append({
                'career': career,
                'match_score': score,
                'explanation': explanation
            })

        # Sort by score descending and return top 5
        recommendations.sort(key=lambda x: x['match_score'], reverse=True)
        return recommendations[:5]

    def _calculate_match_score(self, user_skills, user_interests, user_education, career):
        score = 0
        max_score = 100

        # Skills match (40% weight)
        career_skills = set(career.get('skills', []))
        user_skills_set = set(user_skills)
        skill_match = len(career_skills.intersection(user_skills_set)) / len(career_skills) if career_skills else 0
        score += skill_match * 40

        # Interests match (30% weight)
        career_description = career.get('description', '').lower()
        interest_match = sum(1 for interest in user_interests if interest.lower() in career_description)
        score += (interest_match / len(user_interests)) * 30 if user_interests else 0

        # Education match (20% weight)
        career_education = career.get('education', '').lower()
        if user_education.lower() in career_education:
            score += 20

        # Experience match (10% weight) - simplified
        career_experience = career.get('experience', '')
        if 'entry' in career_experience.lower() or '1' in career_experience:
            score += 10  # Assume beginner friendly

        return min(score, max_score)

    def _generate_explanation(self, score, career):
        if score >= 80:
            return f"Excellent match! Your skills align well with {career['title']}."
        elif score >= 60:
            return f"Good match. Consider developing skills in {', '.join(career.get('skills', []))}."
        elif score >= 40:
            return f"Moderate match. You may need to learn some new skills for {career['title']}."
        else:
            return f"Low match. This career may require significant skill development."