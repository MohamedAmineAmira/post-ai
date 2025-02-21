Let me generate a comprehensive README for your PostAI project:

# PostAI Project Overview

PostAI is a full-stack application that enables users to generate and manage social media posts using artificial intelligence. The project combines a Django backend with a Vue.js frontend to create a seamless experience for generating and managing AI-powered content.

## Core Features

- AI-powered post generation
- User authentication and authorization
- Secure API endpoints
- Responsive frontend interface
- Real-time post management

## Technical Stack

- Backend: Django
- Frontend: Vue.js with Vite
- Database: SqlLite
- API Integration: OpenAI API


## Getting Started

Clone the repository```bash
git clone https://github.com/MohamedAmineAmira/post-ai.git
```

Set up environment variables- Backend: Create `.env` file in backend directory
- Frontend: Create `.env` file in frontend directory

Start services- Run backend server: `cd postit_backend && python manage.py runserver`
- Run frontend development server: `cd frontend && npm run dev`

## Project Structure

post-ai/
├── postit_backend/      # Backend implementation
└── frontend/            # Frontend implementation## Development Guidelines

- Backend API endpoints follow REST conventions
- Frontend components are organized by feature
- State management uses Pinia stores
- API calls are centralized in service modules

## Security Considerations

- Environment variables are required for sensitive data
- Authentication tokens are stored securely
- API requests include proper authorization headers
- Input validation occurs on both frontend and backend

Refer to the respective README files in each directory for detailed setup and implementation details specific to the frontend and backend components.