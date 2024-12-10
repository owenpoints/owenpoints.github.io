set /p commit_message=""

echo MODE: %commit_message%

git add .

git commit -m "%commit_message%"

git push -f

pause