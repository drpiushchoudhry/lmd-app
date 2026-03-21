@echo off
echo Starting backend...

cd backend

start cmd /k python -m uvicorn main:app --reload

cd ..

timeout /t 3

echo Opening frontend...
start index.html

pause