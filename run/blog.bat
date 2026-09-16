@echo off

cd ..\

py -m blog.blog_client

call push.bat "Blog Update"
