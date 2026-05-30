# Create Flask route for feedback
# Endpoint: POST /feedback
# Accept JSON:
# - user_id
# - rating
# - comments
# Call feedback_controller
# Return success message

from flask import Blueprint, request, jsonify
from controllers.feedback_controllers import FeedbackController

feedback_bp = Blueprint('feedback', __name__)
feedback_controller = FeedbackController()

@feedback_bp.route('/feedback', methods=['POST'])
def submit_feedback():
    data = request.get_json()
    if not data:
        return jsonify({'success': False, 'message': 'No data provided'}), 400

    result = feedback_controller.submit_feedback(data)
    status_code = 201 if result['success'] else 400
    return jsonify(result), status_code