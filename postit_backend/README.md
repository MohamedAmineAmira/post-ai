# PostAI Backend

PostAI is the backend for an AI-powered social media post generation platform. Built with Django, it handles user authentication, post management, and communication with the frontend. The backend exposes API endpoints to interact with Generative AI models, allowing users to generate and manage posts.

### Backend Structure

```text
- postit_backend:
  - core: Contains common settings and utility functions for the application.
  - auth: Authentication-related views and URL routes for login, registration, and token refresh.
  - abstract: Includes abstract components and reusable configurations across the application.
  - post: Manages all post-related models, serializers, and API endpoints.
  - user: Contains user-related views and models.
```

## Setup Instructions

### 1. Clone the repository:

```bash
git clone https://github.com/MohamedAmineAmira/post_ai.git
cd post_ai
```

### 2. Backend setup:

Navigate to the postit_backend folder:```bash
cd postit_backend
```

Set up the virtual environment:```bash
python -m venv venv
```

Activate the virtual environment:```bash
# On Linux/macOS:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

Install dependencies:```bash
pip install -r requirements.txt
```

Create a .env file:```bash
echo "OPENAI_API_KEY=your_api_key_here" > .env
```

Apply database migrations:```bash
python manage.py migrate
```

Start the Django server:```bash
python manage.py runserver
```