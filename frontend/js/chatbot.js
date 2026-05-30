// Build chatbot functionality
// Send user message to /chat API
// Display responses in chat UI

document.addEventListener('DOMContentLoaded', function () {
    const chatbotToggle = document.getElementById('chatbot-toggle');
    const chatbotWindow = document.getElementById('chatbot-window');
    const chatInput = document.getElementById('chat-input');
    const chatSend = document.getElementById('chat-send');
    const chatMessages = document.getElementById('chat-messages');

    // Toggle chatbot visibility
    chatbotToggle.addEventListener('click', function () {
        const isVisible = chatbotWindow.style.display === 'flex';
        chatbotWindow.style.display = isVisible ? 'none' : 'flex';
    });

    // Send message on button click
    chatSend.addEventListener('click', sendMessage);

    // Send message on Enter key
    chatInput.addEventListener('keypress', function (e) {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    async function sendMessage() {
        const message = chatInput.value.trim();
        if (!message) return;

        // Add user message to chat
        addMessage(message, 'user');

        // Clear input
        chatInput.value = '';

        // Show typing indicator
        addMessage('Typing...', 'bot', true);

        try {
            // Get context from current page
            const context = getCurrentContext();

            // Send to backend
            const result = await sendChat(message, context);

            // Remove typing indicator
            removeTypingIndicator();

            if (result.success) {
                addMessage(result.data.reply, 'bot');
            } else {
                addMessage('Sorry, I encountered an error. Please try again.', 'bot');
            }
        } catch (error) {
            removeTypingIndicator();
            addMessage('Network error. Please check your connection and try again.', 'bot');
            console.error('Chat error:', error);
        }
    }

    function addMessage(text, sender, isTyping = false) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}`;
        if (isTyping) {
            messageDiv.id = 'typing-indicator';
        }
        messageDiv.textContent = text;
        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    function removeTypingIndicator() {
        const typingIndicator = document.getElementById('typing-indicator');
        if (typingIndicator) {
            typingIndicator.remove();
        }
    }

    function getCurrentContext() {
        // Get context based on current page
        const path = window.location.pathname;
        if (path.includes('dashboard')) {
            return 'User is viewing career recommendations on the dashboard.';
        } else if (path.includes('roadmap')) {
            const career = localStorage.getItem('selectedCareer');
            return `User is viewing the learning roadmap for ${career}.`;
        } else if (path.includes('onboarding')) {
            return 'User is in the onboarding process, providing their skills and interests.';
        }
        return 'User is on the career advisor website.';
    }
});