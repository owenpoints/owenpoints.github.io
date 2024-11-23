@echo off
set /p username="Input github username: "
set /p email="Input github email: "
set /p password="Input github password: "
cls

echo Signing in to Git...
git config --global user.name "%username%"
git config --global user.email "%email%"
git config --global user.password "%password%"
echo Done.

git init
git add ..\

set /p url="Input git repo URL: "
git remote add origin %url%

echo Pushing to GitHub...
git commit -m "First Commit"
git push -f
echo Done.

pause