@echo off

cd ..\

set /p bloguser="Input username to use for blog: "
set empty=""

echo %bloguser% > .\blog\username.txt
echo {} > .\blog\store.txt
echo Run blog.bat to construct your web page. > .\blog\README.md
echo Deleting blog posts...
del .\blog\posts\*.*
echo Deleting saved blog images...
del .\blog\images\*.*

echo %empty% > .\points\log.txt
echo {} > .\points\store.txt
echo Run points.bat to construct your web page. > .\README.md

set /p ownername="Input name to use on site (e.g. to replace Top Owen Updates text): "
set /p pointsname="Input name of points (e.g. Owen Points): "
set /p urltovideoservice="Input url for live execution content channel: "
set /p urltorequestform="Input url to points request form: "

echo Editing file contents to reflect this...
echo "Owen Points:::%pointsname%:::.\points\points_client.py" | python3 -m setup.replacestrings
echo "Owen:::%ownername%:::.\points\points_client.py" | python3 -m setup.replacestrings
echo "https://www.twitch.tv/will_of_owen:::%urltovideoservice%:::.\points\points_client.py" | python3 -m setup.replacestrings
echo "https://forms.gle/cc2Y95JU66t6gKew9:::%urltorequestform%:::.\points\points_client.py" | python3 -m setup.replacestrings

echo "Owen Points:::%pointsname%:::.\blog\blog_client.py" | python3 -m setup.replacestrings
echo "Owen:::%ownername%:::.\blog\blog_client.py" | python3 -m setup.replacestrings
echo Done.

set /p gitusername="Input your GitHub username: "
set /p email="Input the email associated with your GitHub account: "
set /p password="Input your GitHub password: "
set /p repo="Input name of repository: "

git config --global user.email "%email%"
git config --global user.name "%gitusername%"
git config --global user.password "%password%"

cls

git remote add origin https://github.com/%gitusername%/%repo%.git

echo Pushing to GitHub...
git init
git add .
git commit -m "First Commit"
git push --set-upstream origin master
echo Done.

pause
