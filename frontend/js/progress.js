// Track and display user progress
// Fetch progress data from backend
// Update progress bar UI
// Show completed skills and current step
// Handle updates dynamically

document.addEventListener('DOMContentLoaded', function () {
    // Initialize progress tracking
    updateProgressDisplay();

    // Add event listeners for step completion (if buttons exist)
    const completeButtons = document.querySelectorAll('.complete-step-btn');
    completeButtons.forEach(button => {
        button.addEventListener('click', function () {
            const stepId = this.getAttribute('data-step');
            markStepComplete(stepId);
        });
    });
});

function updateProgressDisplay() {
    const progressFill = document.getElementById('progress-fill');
    const progressText = document.getElementById('progress-text');

    if (!progressFill || !progressText) return;

    // Get progress from localStorage (in a real app, this would come from backend)
    const progress = parseInt(localStorage.getItem('userProgress') || '0');

    progressFill.style.width = `${progress}%`;
    progressText.textContent = `${progress}% Complete`;
}

function markStepComplete(stepId) {
    // In a real implementation, this would update the backend
    // For now, we'll simulate progress
    const currentProgress = parseInt(localStorage.getItem('userProgress') || '0');
    const newProgress = Math.min(currentProgress + 25, 100); // Assume each step is 25%

    localStorage.setItem('userProgress', newProgress.toString());
    updateProgressDisplay();

    // Update UI to show step as completed
    const stepElement = document.querySelector(`[data-step="${stepId}"]`);
    if (stepElement) {
        stepElement.classList.add('completed');
        stepElement.querySelector('.complete-step-btn').style.display = 'none';
    }
}

// Function to save progress to backend (placeholder)
async function saveProgress(userId, completedSkills, currentStep, progressPercentage) {
    // This would call the backend API to save progress
    // For now, it's a placeholder
    console.log('Saving progress:', { userId, completedSkills, currentStep, progressPercentage });
}