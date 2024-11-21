import os
import ast

def pretty_num(num):
    out = f'{num:,}'
    return out


def output(store):
    file = open('README.md', 'w')

    output_str = "# Global Owen Points Rankings\n\n|Ranking|Name|Owen Points|\n| ----------- | ----------- | ----------- |\n"
    
    store = dict(sorted(store.items(), key=lambda item: item[1]))
    store = {k: store[k] for k in reversed(store)}

    for i, item in enumerate(store):
        output_str += f"|{i + 1}.|{list(store)[i]}|{pretty_num(store[item])}|\n"

    output_str += "\nReport Someone or Request Points [Here](https://forms.gle/cc2Y95JU66t6gKew9).\n"

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

        scores.remove(remove_choice)
    elif choice == "add":
        scores[input("Input name to add: ")] = 0
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

        scores[edit_choice] += increment
    
    os.system("cls")

output(scores)
save(scores)

store.close()