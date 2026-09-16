@echo off

cd ..\

py -m points.points_client

call push.bat "Automated Points Update"
