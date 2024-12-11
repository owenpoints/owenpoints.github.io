import os
import ast
import datetime
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'assets'))
from assets import *

def output(store):

    file = better_open('./wheel/README.md', 'w')

    output_str = "# Global Wheel Points Rankings\n\n|Ranking|Name|Wheel Points|\n| ----------- | ----------- | ----------- |\n"
    
    store = dict(sorted(store.items(), key=lambda item: item[1]))
    store = {k: store[k] for k in reversed(store)}

    for i, item in enumerate(store):
        output_str += f"|{i + 1}.|{list(store)[i]}|{pretty_num(store[item])}|\n"

    output_str += "\n## 10 Wheel Points can be exchanged for 1 Owen Point\n"

    file.write(output_str)
    file.close()
    
def save(store):
    
    file = better_open('./wheel/store.txt', 'w')

    file.write(str(store))

    file.close()

store = better_open('./wheel/store.txt', 'r')

scores = ast.literal_eval(store.read())

error_message = ''

while True:

    os.system("cls")

    scores = dict(sorted(scores.items(), key=lambda item: item[1]))
    scores = {k: scores[k] for k in reversed(scores)}
    
    for i in scores:

        print(i, ":", scores[i])
    
    if error_message:

        print(f"\n!! {error_message} !!\n")

        error_message = ""

    options = ("edit", "transfer", "help", "exit")
    
    raw_choice = input(f"Input operation {options}: ").strip()

    if not raw_choice:

        error_message = "Please input a command."

        continue

    operation = raw_choice.split()[0]
    arguments = [item.strip() for item in raw_choice.split('"') if item and item != " "]
    arguments.pop(0)
 
    if operation not in options:

        error_message = "Enter valid operation."

        continue

    if operation == "exit":

        break
        
    elif operation == "edit":

        if len(arguments) != 3:

            error_message = "Invalid command arguments, type help for help."
        
            continue


        if arguments[0] not in scores and arguments[0] != "All":
    
            error_message = "Person does not exist."

            continue

        try:
            
            arguments[1] = int(arguments[1].strip())
        
        except ValueError:
            
            error_message = "Input integer for points increment."

            continue
        
        if arguments[0] == "All":
            scores = {key: scores[key] + arguments[1] for key in scores}
        else:
            scores[arguments[0]] += arguments[1]

    elif operation == "transfer":

        if len(arguments) != 4:

            error_message = "Invalid command arguments, type help for help."
        
            continue

        if not (arguments[0] in scores and arguments[1] in scores) and arguments[1] != "All":
    
            error_message = "Person does not exist."

            continue

        try:
            
            arguments[2] = int(arguments[2].strip())
        
        except ValueError:
            
            error_message = "Input integer for points transfer."

            continue
        
        if arguments[1] == "All":
            scores[arguments[0]] -= arguments[2] * len(scores)
            scores = {key : scores[key] + arguments[2] for key in scores}
        else:
            scores[arguments[0]] -= arguments[2]
            scores[arguments[1]] += arguments[2]

    elif operation == "help":

        print('\nOperation: edit , Syntax: edit "name" increment "reason" , Description: Edit points of existing people.')
        print('Operation: transfer , Syntax: transfer "sender" "recipient" amount "reason" , Description: Transfer points between people.')
        print('Operation: help , Syntax: help , Description: Access this help message.')
        print('Operation: exit , Syntax: exit , Description: Exit the program.\n')

        os.system("pause")

output(scores)
save(scores)

store.close()