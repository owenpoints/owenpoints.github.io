@echo off
git init ..\
git add ..\

set \p bloguser="Input username to use for blog: "
set empty=""

echo %bloguser% > ..\blog\username.txt
echo {} > ..\blog\store.txt
echo Run blog.bat to construct your web page. > ..\blog\README.md
del ..\blog\posts\*.*
del ..\blog\images\*.*
del ..\blog\devlog.py

echo %empty% > ..\points\log.txt
echo {} > ..\points\store.txt
echo Run points.bat to construct your web page. > ..\README.md
del ..\favicon.ico

set \p username="Input your GitHub username: "
set \p repo="Input name of repository: "
git remote add origin https://github.com/%username%/%repo%.git

echo Pushing to GitHub...
git commit -m "First Commit"
git push --set-upstream origin master
echo Done.

pause