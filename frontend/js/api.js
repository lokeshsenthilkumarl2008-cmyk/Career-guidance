const API_BASE_URL = 'http://localhost:5000'; // Adjust if needed

async function analyzeUser(data) {
    try {
        const response = await fetch(`${API_BASE_URL}/analyze`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        const result = await response.json();
        return result;
    } catch (error) {
        console.error('Error analyzing user:', error);
        return { success: false, message: 'Network error. Please try again.' };
    }
}

async function getRoadmap(career, skills = null) {
    try {
        let url = `${API_BASE_URL}/roadmap?career=${encodeURIComponent(career)}`;
        if (skills) {
            url += `&skills=${encodeURIComponent(skills.join(','))}`;
        }

        const response = await fetch(url);
        const result = await response.json();
        return result;
    } catch (error) {
        console.error('Error getting roadmap:', error);
        return { success: false, message: 'Network error. Please try again.' };
    }
}

async function sendChat(message, context = null) {
    try {
        const data = { message };
        if (context) {
            data.context = context;
        }

        const response = await fetch(`${API_BASE_URL}/chat`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        const result = await response.json();
        return result;
    } catch (error) {
        console.error('Error sending chat:', error);
        return { success: false, message: 'Network error. Please try again.' };
    }
}

async function createUser(data) {
    try {
        const response = await fetch(`${API_BASE_URL}/user`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        const result = await response.json();
        return result;
    } catch (error) {
        console.error('Error creating user:', error);
        return { success: false, message: 'Network error. Please try again.' };
    }
}

async function submitFeedback(data) {
    try {
        const response = await fetch(`${API_BASE_URL}/feedback`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        const result = await response.json();
        return result;
    } catch (error) {
        console.error('Error submitting feedback:', error);
        return { success: false, message: 'Network error. Please try again.' };
    }
}
