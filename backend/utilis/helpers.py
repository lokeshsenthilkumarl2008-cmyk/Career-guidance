import json
import os

def validate_input(data, required_fields):
    """Validate that required fields are present in data"""
    missing = [field for field in required_fields if field not in data or not data[field]]
    if missing:
        return False, f"Missing required fields: {', '.join(missing)}"
    return True, None

def format_response(success, data=None, message=None):
    """Format API response"""
    response = {'success': success}
    if data is not None:
        response['data'] = data
    if message:
        response['message'] = message
    return response

def load_json_file(path):
    """Load JSON file safely"""
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None
