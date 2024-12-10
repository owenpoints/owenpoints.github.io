@echo off

cd ..\

python3 -m blog.blog_client

call push.bat "Blog Update"
