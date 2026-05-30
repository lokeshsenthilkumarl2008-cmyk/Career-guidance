// Fetch roadmap from backend
// Display steps in timeline format

document.addEventListener('DOMContentLoaded', function () {
    const timeline = document.getElementById('timeline');
    const careerTitle = document.getElementById('career-title');
    const loading = document.getElementById('loading');
    const errorMessage = document.getElementById('error-message');

    // Get selected career from localStorage
    const selectedCareer = localStorage.getItem('selectedCareer');
    const userSkills = localStorage.getItem('userSkills');

    if (!selectedCareer) {
        errorMessage.textContent = 'No career selected. Please go back to the dashboard.';
        loading.style.display = 'none';
        return;
    }

    careerTitle.textContent = `Learning Roadmap for ${selectedCareer}`;

    // Fetch roadmap
    loadRoadmap(selectedCareer, userSkills);
});

async function loadRoadmap(career, skills) {
    const loading = document.getElementById('loading');
    const errorMessage = document.getElementById('error-message');
    const timeline = document.getElementById('timeline');

    try {
        const result = await getRoadmap(career, skills ? skills.split(',') : null);

        if (result.success) {
            loading.style.display = 'none';
            displayRoadmap(result.data);
        } else {
            errorMessage.textContent = result.message;
            loading.style.display = 'none';
        }
    } catch (error) {
        errorMessage.textContent = 'Error loading roadmap.';
        loading.style.display = 'none';
        console.error('Roadmap error:', error);
    }
}

function displayRoadmap(roadmapData) {
    const timeline = document.getElementById('timeline');

    roadmapData.steps.forEach(step => {
        const timelineItem = document.createElement('div');
        timelineItem.className = 'timeline-item';

        timelineItem.innerHTML = `
            <div class="timeline-step">
                <div class="step-title">Step ${step.step}: ${step.title}</div>
                <div class="step-duration">${step.duration}</div>
                <p>${step.description}</p>
                <p><strong>Resources:</strong> ${step.resources.join(', ')}</p>
            </div>
        `;

        timeline.appendChild(timelineItem);
    });
}