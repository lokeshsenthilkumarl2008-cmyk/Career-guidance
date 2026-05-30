
from services.ai_aervice import AIService
from utilis.helpers import format_response

class ChatbotController:
    def __init__(self):
        self.ai_service = AIService()

    def chat_with_user(self, message, context=None):
        if not message:
            return format_response(False, message="Message is required")

        try:
            # Add context for career advice
            prompt = f"You are a career advisor chatbot. Help the user with career-related questions. User message: {message}"
            if context:
                prompt += f" Context: {context}"

            response = self.ai_service.generate_response(prompt)
            return format_response(True, data={'reply': response})
        except Exception as e:
            return format_response(False, message=f"Failed to generate chatbot response: {str(e)}") 
