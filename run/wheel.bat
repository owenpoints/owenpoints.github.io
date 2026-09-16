@echo off

cd ..\

py -m wheel.wheel_points_client

call push.bat "Automated Wheel Points Update"
