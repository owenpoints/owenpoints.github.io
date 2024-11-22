@echo off

python3 script.py

echo "exit" | python3 script.py

git add .

git commit -m "Updating Points"

git push -f

pause