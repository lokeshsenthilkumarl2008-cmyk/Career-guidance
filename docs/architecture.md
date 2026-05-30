# System Architecture

## Overview
The system follows a client-server architecture.

## Components

### Frontend
- HTML, CSS, JavaScript
- Handles user interaction

### Backend
- Flask API
- Processes requests
- Handles AI logic

### Database
- SQLite for storing user data

### AI Layer
- Groq API for generating recommendations

## Flow

User → Frontend → Backend API → AI Service → Response → Frontend

## Modules
- Recommendation Engine
- Skill Gap Analyzer
- Roadmap Generator
- Chatbot

## Scalability
- Can migrate to cloud (AWS, Vercel)
- Can integrate vector DB for better AI