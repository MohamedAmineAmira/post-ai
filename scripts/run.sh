#!/bin/bash

# This script runs both the frontend and backend servers.

# Function to run the backend (Django)
run_backend() {
  echo "Starting backend..."

  # Navigate to the backend directory
  cd ../postit_backend

  # Create virtual environment if it doesn't exist
  if [ ! -d "venv" ]; then
    python -m venv venv  # Create venv if it doesn't exist
  fi

  # Activate virtual environment
  source venv/bin/activate

  # Install backend dependencies
  pip install -r requirements.txt

  # Create .env file if not present and add OPENAI_API_KEY
  if [ ! -f ".env" ]; then
    echo "OPENAI_API_KEY=your_openai_api_key_here" > .env
    echo ".env file created and OPENAI_API_KEY set."
  else
    echo ".env file already exists."
  fi

  # Apply migrations
  python manage.py migrate

  # Run the Django development server
  python manage.py runserver
}

# Function to run the frontend (Vite + Vue)
run_frontend() {
  echo "Starting frontend..."

  # Navigate to the frontend directory
  cd ../postit_frontend

  # Install front-end dependencies
  npm install

  # Run the Vite development server (npm run dev)
  npm run dev
}

# Run both frontend and backend in parallel
run_backend & run_frontend
