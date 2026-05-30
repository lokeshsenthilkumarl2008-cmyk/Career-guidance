# Handle user feedback
# Function: submit_feedback(data)
# Store feedback in database or log
# Accept:
# - user_id
# - rating
# - comments
# Return success response or error message

from database.db import execute_query
from utilis.helpers import validate_input, format_response
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FeedbackController:
    def __init__(self):
        pass

    def submit_feedback(self, data):
        valid, error = validate_input(data, ['user_id', 'rating'])
        if not valid:
            return format_response(False, message=error)

        try:
            user_id = data['user_id']
            rating = data['rating']
            comments = data.get('comments', '')

            if not isinstance(rating, int) or rating < 1 or rating > 5:
                return format_response(False, message="Rating must be an integer between 1 and 5")

            execute_query('INSERT INTO feedback (user_id, rating, comments) VALUES (?, ?, ?)',
                         (user_id, rating, comments))

            logger.info(f"Feedback submitted for user {user_id}")
            return format_response(True, message="Feedback submitted successfully")
        except Exception as e:
            logger.error(f"Error submitting feedback: {str(e)}")
            return format_response(False, message="Failed to submit feedback") 
