
from services.recommendation_services import RecommendationService
from utilis.helpers import validate_input, format_response

class CareerController:
    def __init__(self):
        self.recommendation_service = RecommendationService()

    def analyze_user(self, data):
        # Validate input
        valid, error = validate_input(data, ['skills', 'interests', 'education'])
        if not valid:
            return format_response(False, message=error)

        skills = data['skills'] if isinstance(data['skills'], list) else data['skills'].split(',')
        interests = data['interests'] if isinstance(data['interests'], list) else data['interests'].split(',')
        education = data['education']

        # Get recommendations
        recommendations = self.recommendation_service.recommend_careers(skills, interests, education)

        # Format response
        response_data = []
        for rec in recommendations:
            response_data.append({
                'career': rec['career']['title'],
                'match_score': rec['match_score'],
                'explanation': rec['explanation'],
                'description': rec['career']['description'],
                'skills': rec['career']['skills']
            })

        return format_response(True, data={'careers': response_data})
