# Create Flask routes for user operations
# Endpoints:
# POST /user → create user
# GET /user/<id> → get user details
# PUT /user/<id> → update user
# Call user_controller functions
# Return JSON responses

from flask import Blueprint, request, jsonify
from controllers.user_controllers import UserController

user_bp = Blueprint('user', __name__)
user_controller = UserController()

@user_bp.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data:
        return jsonify({'success': False, 'message': 'No data provided'}), 400

    result = user_controller.create_user(data)
    status_code = 201 if result['success'] else 400
    return jsonify(result), status_code

@user_bp.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    result = user_controller.get_user(user_id)
    status_code = 200 if result['success'] else 404
    return jsonify(result), status_code

@user_bp.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    if not data:
        return jsonify({'success': False, 'message': 'No data provided'}), 400

    result = user_controller.update_user(user_id, data)
    status_code = 200 if result['success'] else 400
    return jsonify(result), status_code