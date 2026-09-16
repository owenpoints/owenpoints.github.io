@echo off

pushd %~dp0

cd ..\

py -m blog.devlog_client

call push.bat "Codebase Update"

popd