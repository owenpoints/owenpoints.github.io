@echo off

cd ..\

py -m blog.devlog_client

call push.bat "Codebase Update"
