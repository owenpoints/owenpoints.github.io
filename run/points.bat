@echo off

pushd %~dp0

cd ..\

py -m points.points_client

call push.bat "Automated Points Update"

popd