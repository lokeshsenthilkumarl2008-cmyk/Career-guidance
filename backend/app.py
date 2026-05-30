"""
Project: One Stop Personalized Career and Educational Adviser

Backend: Flask
Frontend: HTML, CSS, JavaScript
Database: SQLite
AI: Groq API

Goal:
Build an AI-powered system that:
- Takes user skills, interests, education
- Suggests best career paths
- Explains why each career fits
- Identifies skill gaps
- Generates a learning roadmap
- Provides chatbot support
- Tracks user progress

Architecture:
- Routes → Controllers → Services → Models → Database
- Services contain core logic (AI, recommendations, roadmap)

Requirements:
- Modular, clean, production-ready code
- Proper error handling
- JSON-based APIs
- Scalable structure

Generate the Flask app accordingly with all routes registered.
"""

from flask import Flask
from flask_cors import CORS
from config import FLASK_CONFIG
from database.db import init_db

# Import blueprints
from routes.career_routes import career_bp
from routes.user_routes import user_bp
from routes.roadmap_routes import roadmap_bp
from routes.chatbot_routes import chatbot_bp
from routes.feedback_routes import feedback_bp
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message")

    return jsonify({
        "reply": f"You said: {user_message}"
    })

def create_app():
    app = Flask(__name__)
    app.config.update(FLASK_CONFIG)

    # Enable CORS
    CORS(app)

    # Initialize database
    with app.app_context():
        init_db()

    # Register blueprints
    app.register_blueprint(career_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(roadmap_bp)
    app.register_blueprint(chatbot_bp)
    app.register_blueprint(feedback_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)