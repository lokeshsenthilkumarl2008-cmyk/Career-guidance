# Create chatbot endpoint
# POST /chat
# Input: user message
# Call ai_service to generate response
# Return chatbot reply

from flask import Blueprint, request, jsonify
from controllers.chatbot_controllers import ChatbotController

chatbot_bp = Blueprint('chatbot', __name__)
chatbot_controller = ChatbotController()

@chatbot_bp.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({'success': False, 'message': 'Message is required'}), 400

    message = data['message']
    context = data.get('context')

    result = chatbot_controller.chat_with_user(message, context)
    status_code = 200 if result['success'] else 500
    return jsonify(result), status_code