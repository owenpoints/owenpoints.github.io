@echo off

set /p bloguser="Input username to use for blog: "
set empty=""

echo %bloguser% > ..\blog\username.txt
echo {} > ..\blog\store.txt
echo Run blog.bat to construct your web page. > ..\blog\README.md
del ..\blog\posts\*.*
del ..\blog\images\*.*

echo %empty% > ..\points\log.txt
echo {} > ..\points\store.txt
echo Run points.bat to construct your web page. > ..\README.md


set /p username="Input your GitHub username: "
set /p email="Input the email associated with your GitHub account: "
set /p repo="Input name of repository: "

git config --global user.email "%email%"
git config --global user.name "%username%"

git remote add origin https://github.com/%username%/%repo%.git

echo Pushing to GitHub...
git init ..\
git add ..\
git commit -m "First Commit"
git push --set-upstream origin master
echo Done.

pause