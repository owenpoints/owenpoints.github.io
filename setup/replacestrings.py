from assets import *

to_replace, replacement, file_path = input().strip().split(":::")

f = better_open(file_path, 'r')
contents = f.read()
f.close()

contents = contents.replace(to_replace, replacement)

f = better_open(file_path, 'w')
f.write(contents)
f.close()
