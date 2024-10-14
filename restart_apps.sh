#!/bin/bash

# Navigate to Django project directory
cd /Users/nur/testLab/django_project

# Activate virtual environment
source venv/bin/activate

# Kill any running Django server
pkill -f runserver

# Start Django server
python manage.py runserver &

# Wait for a moment to ensure Django is running
sleep 5

# Navigate to React project directory
cd /Users/nur/testLab/chatgpt-app

# Kill any running React server on port 3000
PID=$(lsof -t -i:3000)
if [ -n "$PID" ]; then
  echo "Killing process on port 3000 (PID: $PID)"
  kill -9 $PID
fi

# Start React server
npm start &
