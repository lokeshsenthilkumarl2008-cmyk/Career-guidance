// Display career suggestions
// Show:
// - career name
// - match percentage
// - explanation
// - missing skills

document.addEventListener('DOMContentLoaded', function () {
    const careerCards = document.getElementById('career-cards');
    const loading = document.getElementById('loading');
    const errorMessage = document.getElementById('error-message');

    // Load career results from localStorage
    const careerResults = localStorage.getItem('careerResults');
    const userData = localStorage.getItem('userData');

    if (!careerResults) {
        errorMessage.textContent = 'No career data found. Please complete the onboarding process.';
        loading.style.display = 'none';
        return;
    }

    try {
        const careers = JSON.parse(careerResults);
        const user = JSON.parse(userData);

        loading.style.display = 'none';

        careers.forEach(career => {
            const card = createCareerCard(career, user);
            careerCards.appendChild(card);
        });

    } catch (error) {
        errorMessage.textContent = 'Error loading career data.';
        loading.style.display = 'none';
        console.error('Dashboard error:', error);
    }
});

function createCareerCard(career, user) {
    const card = document.createElement('div');
    card.className = 'career-card';

    card.innerHTML = `
        <h3>${career.career}</h3>
        <div class="match-score">${career.match_score.toFixed(1)}% Match</div>
        <p><strong>Description:</strong> ${career.description}</p>
        <p><strong>Why it fits:</strong> ${career.explanation}</p>
        <p><strong>Key Skills:</strong> ${career.skills.join(', ')}</p>
        <button class="view-roadmap-btn" data-career="${career.career}">View Learning Roadmap</button>
    `;

    // Add event listener for roadmap button
    const roadmapBtn = card.querySelector('.view-roadmap-btn');
    roadmapBtn.addEventListener('click', function () {
        const selectedCareer = this.getAttribute('data-career');
        localStorage.setItem('selectedCareer', selectedCareer);
        localStorage.setItem('userSkills', user.skills);
        window.location.href = 'roadmap.html';
    });

    return card;
}