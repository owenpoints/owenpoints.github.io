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

    choice = input("Input operation (edit, add, remove, exit): ")

    if choice == "exit":
        break
    elif choice == "remove":
        scores.remove(input("Input person to remove: "))
    elif choice == "add":
        scores[input("Input name to add: ")] = 0
    elif choice == "edit":
        scores[input("Input person to edit: ")] += int(input("Input number to increment by: "))
    
    os.system("cls")

output(scores)
save(scores)

store.close()