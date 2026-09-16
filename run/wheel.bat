@echo off

pushd %~dp0

cd ..\

py -m wheel.wheel_points_client

call push.bat "Automated Wheel Points Update"

popd