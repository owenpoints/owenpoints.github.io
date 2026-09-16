@echo off

cd ..\

python3 -m blog.devlog_client

call push.bat "Codebase Update"
