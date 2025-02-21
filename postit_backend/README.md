# 🚀 PostAI Backend

PostAI is the backend for an AI-powered social media post generation platform. Built with **Django**, it handles user authentication, post management, and communication with the frontend. The backend exposes **API endpoints** to interact with Generative AI models, allowing users to generate and manage posts.

## 🏗 Backend Structure

```plaintext
- postit_backend/
  ├── core/       # Common settings and utility functions
  ├── auth/       # Authentication (login, registration, token refresh)
  ├── abstract/   # Abstract components and reusable configurations
  ├── post/       # Post-related models, serializers, and API endpoints
  ├── user/       # User-related views and models
```

---

## 🔧 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/MohamedAmineAmira/post_ai.git
cd post_ai
```

### 2️⃣ Backend Setup

Navigate to the **backend directory**:

```bash
cd postit_backend
```

Set up a **virtual environment**:

```bash
python -m venv venv
```

Activate the virtual environment:

```bash
# On Linux/macOS:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a **`.env` file**:

```bash
echo "OPENAI_API_KEY=your_api_key_here" > .env
```

Apply **database migrations**:

```bash
python manage.py migrate
```

Start the **Django development server**:

```bash
python manage.py runserver
```

---

## ✅ Next Steps

- Configure environment variables properly in `.env`
- Ensure **database setup** is correct (`sqlite` by default, change if needed)
- Implement authentication and API testing with **Postman** or **cURL**
- Connect the frontend to the backend via API requests

---

📌 **Author:** [Mohamed Amine Amira](https://github.com/MohamedAmineAmira)  
📌 **License:** MIT

