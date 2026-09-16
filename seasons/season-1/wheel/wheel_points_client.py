import os
import ast
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'assets'))
from assets import *
from wheel.wheel_assets import *

store = better_open('./points/store.txt', 'r')

op_scores = ast.literal_eval(store.read())

store.close()

store = better_open('./wheel/store.txt', 'r')

scores = ast.literal_eval(store.read())

for key in op_scores:

    if key not in scores:

        scores[key] = 0

for key in scores:

    if key not in op_scores:

        scores.pop(key)

error_message = ''

while True:

    os.system("cls")

    scores = dict(sorted(scores.items(), key=lambda item: item[1]))
    scores = {k: scores[k] for k in reversed(scores)}
    scores = pretty_dict(scores)

    for i in scores:

        print(i, ":", scores[i])
    
    if error_message:

        print(f"\n!! {error_message} !!\n")

        error_message = ""

    options = ("edit", "transfer", "quickspin", "help", "exit")
    
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

        if len(arguments) != 2:

            error_message = "Invalid command arguments, type help for help."
        
            continue


        if arguments[0] not in scores and arguments[0] != "All":
    
            error_message = "Person does not exist."

            continue

        try:
            
            arguments[1] = float(arguments[1].strip())
        
        except ValueError:
            
            error_message = "Input float for points increment."

            continue
        
        if arguments[0] == "All":

            scores = {key: scores[key] + arguments[1] for key in scores}

        else:

            scores[arguments[0]] += arguments[1]

    elif operation == "transfer":

        if len(arguments) != 3:

            error_message = "Invalid command arguments, type help for help."
        
            continue

        if not (arguments[0] in scores and arguments[1] in scores) and arguments[1] != "All":
    
            error_message = "Person does not exist."

            continue

        try:
            
            arguments[2] = float(arguments[2].strip())
        
        except ValueError:
            
            error_message = "Input float for points transfer."

            continue
        
        if arguments[1] == "All":

            scores[arguments[0]] -= arguments[2] * len(scores)
            scores = {key : scores[key] + arguments[2] for key in scores}

        else:

            scores[arguments[0]] -= arguments[2]
            scores[arguments[1]] += arguments[2]

    elif operation == "quickspin":

        if len(arguments) != 2:

            error_message = "Invalid command arguments, type help for help."
        
            continue


        if arguments[0] not in scores and arguments[0] != "All":
    
            error_message = "Person does not exist."

            continue

        try:
            
            arguments[1] = int(arguments[1].strip())
        
        except ValueError:
            
            error_message = "Input integer for wheel spins."

            continue
        
        increment = quick_spin(arguments[1])
        error_message = f"You got {increment} wheel points."

        if arguments[0] == "All":

            scores = {key: scores[key] + increment for key in scores}

        else:

            scores[arguments[0]] += increment



    elif operation == "help":

        print('\nOperation: edit , Syntax: edit "name" increment , Description: Edit points of people.')
        print('Operation: transfer , Syntax: transfer "sender" "recipient" amount , Description: Transfer points between people.')
        print('Operation: quickspin , Syntax: quickspin "name" spins , Description: Spin the wheel multiple times quickly.')
        print('Operation: help , Syntax: help , Description: Access this help message.')
        print('Operation: exit , Syntax: exit , Description: Exit the program.\n')

        os.system("pause")

wheel_output(scores)

wheel_save(scores)

store.close()