@echo off

cd ..\

python3 -m wheel.wheel_points_client

call push.bat "Automated Wheel Points Update"
