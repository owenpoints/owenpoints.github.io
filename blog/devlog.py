import os
import datetime

user = open('./blog/username.txt', 'r')
username = user.read()
user.close()

def send_to_log(message):
    log = open('./blog/posts/Devlog Post.md', 'r')
    content = log.read()
    log.close()

    content = content[14:]

    log = open('./blog/posts/Devlog Post.md', 'w')
    log.seek(0,0)
    log.write(f'# Devlog Post\n{message}\n\n{content}')
    log.close()

    
while True:

    options = ("add", "exit")
    while True:
        choice = input(f"Input operation {options}: ").strip()
        if choice in options:
            break
        print("Enter valid option.")

    if choice == "exit":
        break
    elif choice == "add":

        
        post = input("Input log post: ")
            
        
        send_to_log(f'{datetime.datetime.now()} \| {username} \| {post}')
    os.system("cls")
