# Frontend Setup

The frontend is built using Vue.js with Vite for fast development. It allows users to interact with the backend and generate posts.

### Project Structure

```text
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

## Setup Instructions

Create a new Vue.js project with Vite```bash
npm create vite@latest frontend -- --template vue
cd frontend
```

Install dependencies```bash
npm install vue-router axios
```

Configure environment variablesCreate a `.env` file in the project root:

```env
VITE_API_URL=http://localhost:8000/
```

Start the development server```bash
npm run dev
```

The frontend will now be running at `http://localhost:5173` and will communicate with the backend at `http://localhost:8000/api/`. Make sure the backend server is running before accessing protected routes.