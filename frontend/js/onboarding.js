// Capture user input (skills, interests, education)
// Send data to backend /analyze API
// Redirect to dashboard with results

document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('onboarding-form');
    const errorMessage = document.getElementById('error-message');

    form.addEventListener('submit', async function (e) {
        e.preventDefault();

        // Clear previous error
        errorMessage.textContent = '';

        // Get form data
        const formData = new FormData(form);
        const data = {
            name: formData.get('name'),
            skills: formData.get('skills'),
            interests: formData.get('interests'),
            education: formData.get('education')
        };

        // Validate
        if (!data.name || !data.skills || !data.interests || !data.education) {
            errorMessage.textContent = 'Please fill in all fields.';
            return;
        }

        // Show loading
        const submitBtn = form.querySelector('button[type="submit"]');
        const originalText = submitBtn.textContent;
        submitBtn.textContent = 'Analyzing...';
        submitBtn.disabled = true;

        try {
            // Create user first
            const userResult = await createUser(data);
            if (!userResult.success) {
                throw new Error(userResult.message);
            }

            // Store user ID for later use
            localStorage.setItem('userId', userResult.data.user_id);

            // Analyze for career recommendations
            const analysisResult = await analyzeUser({
                skills: data.skills.split(',').map(s => s.trim()),
                interests: data.interests.split(',').map(s => s.trim()),
                education: data.education
            });

            if (analysisResult.success) {
                // Store results and redirect
                localStorage.setItem('careerResults', JSON.stringify(analysisResult.data.careers));
                localStorage.setItem('userData', JSON.stringify(data));
                window.location.href = 'dashboard.html';
            } else {
                errorMessage.textContent = analysisResult.message;
            }
        } catch (error) {
            errorMessage.textContent = 'An error occurred. Please try again.';
            console.error('Onboarding error:', error);
        } finally {
            submitBtn.textContent = originalText;
            submitBtn.disabled = false;
        }
    });
});