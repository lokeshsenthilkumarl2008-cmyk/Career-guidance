# Create Flask routes for career recommendations
# Endpoint: POST /analyze
# Input: JSON with skills, interests, education
# Call career_controller to process request
# Return career suggestions, explanation, and match score
# Handle invalid input and errors

from flask import Blueprint, request, jsonify
from controllers.career_controllers import CareerController

career_bp = Blueprint('career', __name__)
career_controller = CareerController()

@career_bp.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    if not data:
        return jsonify({'success': False, 'message': 'No data provided'}), 400

    result = career_controller.analyze_user(data)
    status_code = 200 if result['success'] else 400
    return jsonify(result), status_code