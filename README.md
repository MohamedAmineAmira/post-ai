# 🚀 PostAI Backend & Frontend

PostAI is an AI-powered social media post generation platform. The backend, built with **Django**, handles authentication, post management, and AI communication. The frontend, developed with **Vue.js** and **Vite**, provides an interactive interface for users.

---

## 🏗 Backend Structure

```plaintext
- postit_backend/
  ├── core/       # Common settings and utility functions
  ├── auth/       # Authentication (login, registration, token refresh)
  ├── abstract/   # Abstract components and reusable configurations
  ├── post/       # Post-related models, serializers, and API endpoints
  ├── user/       # User-related views and models
```

## 🏗 Frontend Structure

```plaintext
src/
├── assets/                    # Static assets (images, logos)
├── components/                # Reusable UI components
├── Landing/                   # Landing page components
│   ├── Navbar.vue
│   ├── HeroSection.vue
│   ├── Features.vue
│   ├── About.vue
│   └── Footer.vue
├── pages/                     # Main application pages
│   ├── LandingPage.vue       # Combines landing components
│   ├── LoginPage.vue         # Login form
│   ├── RegisterPage.vue      # Registration form
│   └── HomePage.vue          # Main interface with PostForm and GeneratedPost
├── router/                   # Routing configuration
│   └── index.js              # Route definitions
├── services/                 # Service utilities
│   └── axiosInstance.js      # Centralized Axios instance
├── App.vue                   # Root component
├── main.js                   # Application entry point
└── styles/                   # Global styles
```

---

## 🔧 Backend Setup Instructions

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

## 🔧 Frontend Setup Instructions

### 1️⃣ Create the Vue.js Project

```bash
npm create vite@latest frontend -- --template vue
cd frontend
```

### 2️⃣ Install Dependencies

```bash
npm install vue-router axios
```

### 3️⃣ Configure Environment Variables

Create a **`.env` file** in the project root:

```env
VITE_API_URL=http://localhost:8000/
```

### 4️⃣ Start the Development Server

```bash
npm run dev
```

The frontend will now be running at `http://localhost:5173` and will communicate with the backend at `http://localhost:8000/api/`. Ensure the backend server is running before accessing protected routes.

---
---

📌 **Author:** [Mohamed Amine Amira](https://github.com/MohamedAmineAmira)  
📌 **License:** MIT

