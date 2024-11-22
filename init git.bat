@echo off
set /p username="Input github username: "
set /p email="Input github email: "
set /p password="Input github password: "
cls

echo Creating Repository...
git config --global user.name "%username%"
git config --global user.email "%email%"
git config --global user.password "%password%"

git init

git add.

set /p url="Input git repo URL: "
git remote add origin %url%
echo Done.

echo Pushing to GitHub...
git commit -m "First Commit"
git push -f
echo Done.

pause