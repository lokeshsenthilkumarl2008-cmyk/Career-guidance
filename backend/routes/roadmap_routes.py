from flask import Blueprint, request, jsonify
from controllers.roadmap_controllers import RoadmapController

roadmap_bp = Blueprint('roadmap', __name__)
roadmap_controller = RoadmapController()

@roadmap_bp.route('/roadmap', methods=['GET'])
def get_roadmap():
    career_name = request.args.get('career')
    user_skills = request.args.get('skills')

    if user_skills:
        user_skills = user_skills.split(',')

    result = roadmap_controller.get_roadmap(career_name, user_skills)
    status_code = 200 if result['success'] else 400
    return jsonify(result), status_code
