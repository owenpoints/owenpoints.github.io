to_replace, replacement, file_path = input().strip().split(":::")

f = open(file_path, 'r')
contents = f.read()
f.close()

contents = contents.replace(to_replace, replacement)

f = open(file_path, 'w')
f.write(contents)
f.close()
