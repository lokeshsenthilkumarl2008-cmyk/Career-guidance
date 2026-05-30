
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    skills TEXT,  -- JSON array of user skills
    interests TEXT,  -- JSON array of user interests
    education TEXT,
    progress TEXT,  -- JSON object for user progress data
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Create careers table
-- Stores career information including required skills and descriptions
CREATE TABLE IF NOT EXISTS careers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    category TEXT,
    description TEXT,
    skills TEXT,  -- JSON array of required skills
    education TEXT,
    experience TEXT,
    salary_range TEXT,
    job_growth TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Create progress table
-- Tracks user progress in their career development journey
CREATE TABLE IF NOT EXISTS progress (
    user_id INTEGER PRIMARY KEY,
    completed_skills TEXT,  -- JSON array of completed skills
    current_step TEXT,
    progress_percentage REAL DEFAULT 0.0,
    roadmap TEXT,  -- JSON object for learning roadmap
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
);

-- Create feedback table
-- Stores user feedback and ratings for the platform
CREATE TABLE IF NOT EXISTS feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    rating INTEGER CHECK (rating >= 1 AND rating <= 5),
    comments TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE SET NULL
);

-- Create chatbot_history table (optional)
-- Stores conversation history for the AI chatbot
CREATE TABLE IF NOT EXISTS chatbot_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    user_message TEXT,
    bot_response TEXT,
    context TEXT,  -- JSON object for conversation context
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
);

-- Create indexes for better query performance
CREATE INDEX IF NOT EXISTS idx_users_name ON users (name);
CREATE INDEX IF NOT EXISTS idx_careers_category ON careers (category);
CREATE INDEX IF NOT EXISTS idx_feedback_user_id ON feedback (user_id);
CREATE INDEX IF NOT EXISTS idx_chatbot_history_user_id ON chatbot_history (user_id);

-- Insert initial career data from careers.json
INSERT OR IGNORE INTO careers (id, title, category, description, skills, education, experience, salary_range, job_growth) VALUES
(1, 'Software Engineer', 'Engineering', 'Designs, develops, and maintains software applications.', '["Python", "REST APIs", "Databases", "Unit Testing", "Git"]', 'Bachelor''s degree in Computer Science or related field', '2+ years of software development experience', '70,000-120,000', 'High'),
(2, 'Data Analyst', 'Data', 'Analyzes data to help businesses make informed decisions.', '["SQL", "Excel", "Tableau", "Python", "Data Visualization"]', 'Bachelor''s degree in Statistics, Mathematics, or equivalent', '1+ years of data analytics experience', '55,000-90,000', 'High'),
(3, 'Product Manager', 'Product', 'Defines product vision and leads cross-functional teams to deliver value.', '["Roadmapping", "Stakeholder Management", "Agile", "User Research", "Prioritization"]', 'Bachelor''s degree in Business or related field', '3+ years product or project management experience', '85,000-140,000', 'Moderate');

-- Create triggers for updating timestamps
CREATE TRIGGER IF NOT EXISTS update_users_timestamp
    AFTER UPDATE ON users
    FOR EACH ROW
    BEGIN
        UPDATE users SET updated_at = CURRENT_TIMESTAMP WHERE id = NEW.id;
    END;

CREATE TRIGGER IF NOT EXISTS update_progress_timestamp
    AFTER UPDATE ON progress
    FOR EACH ROW
    BEGIN
        UPDATE progress SET updated_at = CURRENT_TIMESTAMP WHERE user_id = NEW.user_id;
    END;
