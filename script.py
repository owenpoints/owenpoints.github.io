import os
import ast
import datetime

def pretty_num(num):
    out = f'{num:,}'
    return out

def send_to_log(message):
    log = open('log.txt', 'r')
    content = log.read()
    log.close()

    log = open('log.txt', 'w')
    log.seek(0,0)
    log.write(message + '\n' + content)
    log.close()

def output(store):

    file = open('README.md', 'w')

    output_str = "# Global Owen Points Rankings\n\n|Ranking|Name|Owen Points|\n| ----------- | ----------- | ----------- |\n"
    
    store = dict(sorted(store.items(), key=lambda item: item[1]))
    store = {k: store[k] for k in reversed(store)}

    for i, item in enumerate(store):
        output_str += f"|{i + 1}.|{list(store)[i]}|{pretty_num(store[item])}|\n"

    output_str += "\n## Report Someone or Request Points [Here](https://forms.gle/cc2Y95JU66t6gKew9).\n"
    output_str += "\n## Those Under -500 Owen Points will be Publically Executed via Firing Squad\n\n\n## Owen Points Log:\n"

    log = open('log.txt', 'r')
    lines = log.readlines()
    for i in lines:
        output_str += i + '\n'
    log.close()

    file.write(output_str)
    file.close()
    
def save(store):
    file = open('store.txt', 'w')

    file.write(str(store))

    file.close()

store = open('store.txt', 'r')

scores = ast.literal_eval(store.read())

while True:

    for i in scores:
        print(i, ":", scores[i])

    options = ("edit", "add", "remove", "exit")
    while True:
        choice = input(f"Input operation {options}: ")
        if choice in options:
            break
        print("Enter valid option.")

    if choice == "exit":
        break
    elif choice == "remove":

        while True:
            remove_choice = input("Input person to remove: ")
            if remove_choice in scores:
                break
            print("Enter Valid option.")

        scores.pop(remove_choice)
        
        send_to_log(f'{datetime.datetime.now()} \| Remove \| {remove_choice}')

    elif choice == "add":
        name = input("Input name to add: ")
        scores[name] = 0
        send_to_log(f'{datetime.datetime.now()} \| Add \| {name}')
    elif choice == "edit":

        while True:
            edit_choice = input("Input person to edit: ")
            if edit_choice in scores:
                break
            print("Enter Valid option.")

        while True:
            increment = input("Input points to change by: ")
            try:
                increment = int(increment)
                break
            except ValueError:
                print("Enter an integer.")

        reason = input("Input reason: ")

        scores[edit_choice] += increment

        send_to_log(f'{datetime.datetime.now()} \| Edit Points \| {edit_choice} \| Change: {pretty_num(increment)} \| "{reason}"')
    
    os.system("cls")

output(scores)
save(scores)

store.close()