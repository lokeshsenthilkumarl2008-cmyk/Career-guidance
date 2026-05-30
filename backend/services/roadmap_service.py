# Generate learning roadmap for a career
# Input: career + missing skills
# Output: step-by-step roadmap
# Example:
# Step 1 → Learn basics
# Step 2 → Build project
# Step 3 → Advanced topics

from models.carrier_model import CareerModel

class RoadmapService:
    def __init__(self):
        self.career_model = CareerModel()

    def generate_roadmap(self, career_name, missing_skills):
        career = self.career_model.get_career_by_name(career_name)
        if not career:
            return {'error': 'Career not found'}

        roadmap = {
            'career': career_name,
            'steps': []
        }

        # Basic step
        roadmap['steps'].append({
            'step': 1,
            'title': 'Learn Basics',
            'description': f'Gain foundational knowledge in {career_name}. Study core concepts and principles.',
            'duration': '1-3 months',
            'resources': ['Online courses', 'Books', 'Tutorials']
        })

        # Intermediate step
        roadmap['steps'].append({
            'step': 2,
            'title': 'Develop Core Skills',
            'description': f'Focus on essential skills: {", ".join(career.get("skills", [])[:3])}. Practice through exercises.',
            'duration': '2-6 months',
            'resources': ['Practice projects', 'Coding challenges', 'Certifications']
        })

        # Advanced step
        roadmap['steps'].append({
            'step': 3,
            'title': 'Advanced Topics and Specialization',
            'description': 'Dive deeper into advanced concepts and specialize in a niche area.',
            'duration': '3-12 months',
            'resources': ['Advanced courses', 'Research papers', 'Industry projects']
        })

        # Project step
        roadmap['steps'].append({
            'step': 4,
            'title': 'Build Projects and Gain Experience',
            'description': 'Apply knowledge by building real-world projects. Contribute to open-source or freelance.',
            'duration': 'Ongoing',
            'resources': ['Personal projects', 'Open-source contributions', 'Internships']
        })

        # Address missing skills
        if missing_skills:
            roadmap['steps'].insert(1, {
                'step': 1.5,
                'title': 'Bridge Skill Gaps',
                'description': f'Learn missing skills: {", ".join(missing_skills)}. Use targeted resources.',
                'duration': '1-2 months',
                'resources': ['Specialized courses', 'Bootcamps', 'Mentorship']
            })

        return roadmap