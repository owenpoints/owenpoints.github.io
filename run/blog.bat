@echo off

pushd %~dp0

cd ..\

py -m blog.blog_client

call push.bat "Blog Update"

popd