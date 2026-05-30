# Handle user-related logic
# Functions:
# - create_user(data)
# - get_user(user_id)
# - update_user(user_id, data)
# Interact with user_model
# Validate input data
# Return JSON-friendly responses
# Handle errors and edge cases (e.g., user not found, invalid data)
# Use logging for debugging and monitoring
# Consider security best practices (e.g., password hashing, input sanitization)
# Integrate with authentication system if needed (e.g., JWT tokens)
# Ensure code is modular and maintainable for future features (e.g., user preferences, history)
#  Implement unit tests for user_controller functions to ensure reliability and catch bugs early.

from models.user_model import UserModel
from utilis.helpers import validate_input, format_response
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class UserController:
    def __init__(self):
        self.user_model = UserModel()

    def create_user(self, data):
        valid, error = validate_input(data, ['name', 'skills', 'interests', 'education'])
        if not valid:
            return format_response(False, message=error)

        try:
            skills = data['skills'] if isinstance(data['skills'], list) else data['skills'].split(',')
            interests = data['interests'] if isinstance(data['interests'], list) else data['interests'].split(',')
            user_id = self.user_model.create_user(data['name'], skills, interests, data['education'])
            logger.info(f"Created user with ID: {user_id}")
            return format_response(True, data={'user_id': user_id}, message="User created successfully")
        except Exception as e:
            logger.error(f"Error creating user: {str(e)}")
            return format_response(False, message="Failed to create user")

    def get_user(self, user_id):
        try:
            user = self.user_model.get_user(user_id)
            if user:
                return format_response(True, data=user)
            else:
                return format_response(False, message="User not found")
        except Exception as e:
            logger.error(f"Error getting user {user_id}: {str(e)}")
            return format_response(False, message="Failed to retrieve user")

    def update_user(self, user_id, data):
        try:
            success = self.user_model.update_user(user_id, data)
            if success:
                logger.info(f"Updated user {user_id}")
                return format_response(True, message="User updated successfully")
            else:
                return format_response(False, message="User not found or no changes made")
        except Exception as e:
            logger.error(f"Error updating user {user_id}: {str(e)}")
            return format_response(False, message="Failed to update user")
