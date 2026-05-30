# Handle roadmap generation logic
# Function: get_roadmap(career_name)
# Call roadmap_service
# Return structured roadmap steps
# Handle invalid career input and errors

from services.roadmap_service import RoadmapService
from services.skill_gap_service import SkillGapService
from utilis.helpers import format_response

class RoadmapController:
    def __init__(self):
        self.roadmap_service = RoadmapService()
        self.skill_gap_service = SkillGapService()

    def get_roadmap(self, career_name, user_skills=None):
        if not career_name:
            return format_response(False, message="Career name is required")

        try:
            missing_skills = []
            if user_skills:
                gap_analysis = self.skill_gap_service.analyze_skill_gap(career_name, user_skills)
                if 'error' not in gap_analysis:
                    missing_skills = gap_analysis['missing_skills']

            roadmap = self.roadmap_service.generate_roadmap(career_name, missing_skills)
            if 'error' in roadmap:
                return format_response(False, message=roadmap['error'])

            return format_response(True, data=roadmap)
        except Exception as e:
            return format_response(False, message=f"Failed to generate roadmap: {str(e)}")
