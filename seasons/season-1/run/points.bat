@echo off

cd ..\

python3 -m points.points_client

call push.bat "Automated Points Update"
