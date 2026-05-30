def calculate_score(user_skills, career_skills):
    """
    Calculate the percentage match between user skills and career required skills.

    Args:
        user_skills (list): List of skills the user has.
        career_skills (list): List of skills required for the career.

    Returns:
        float: Percentage match (0-100).
    """
    if not career_skills:
        return 0.0

    # Convert to sets for intersection
    user_set = set(user_skills)
    career_set = set(career_skills)

    # Calculate overlap
    overlap = len(user_set.intersection(career_set))

    # Calculate percentage
    score = (overlap / len(career_set)) * 100

    return round(score, 2)
