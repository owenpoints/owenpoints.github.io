import os
import ast
import datetime
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'assets'))
from assets import *

def send_to_log(message):

    log = better_open('./points/log.txt', 'r')
    content = log.read()
    log.close()

    log = better_open('./points/log.txt', 'w')
    log.write(message + '\n' + content)
    log.close()

def output(store):

    file = better_open('README.md', 'w')

    output_str = "# Global Owen Points Rankings\n\n|Ranking|Name|Owen Points|\n| ----------- | ----------- | ----------- |\n"
    
    store = dict(sorted(store.items(), key=lambda item: item[1]))
    store = {k: store[k] for k in reversed(store)}

    for i, item in enumerate(store):
        output_str += f"|{i + 1}.|{list(store)[i]}|{pretty_num(store[item])}|\n"

    output_str += "\n## Report Someone or Request Points [Here](https://forms.gle/cc2Y95JU66t6gKew9).\n"
    output_str += "\n## !! Those Under -500 Owen Points will be [Executed Live](https://www.twitch.tv/will_of_owen) !!\n"
    output_str += "\n## Top Owen Updates Can be Found [Here](./blog).\n"
    output_str += "\n## Wheel Points Leaderboard can be found [Here](./wheel)\n"
    output_str += "\n\n## Owen Points Log:\n"

    log = better_open('./points/log.txt', 'r')
    lines = log.readlines()
    for i in lines:
        output_str += i + '\n'
    log.close()

    file.write(output_str)
    file.close()
    
def save(store):
    
    file = better_open('./points/store.txt', 'w')

    file.write(str(store))

    file.close()

store = better_open('./points/store.txt', 'r')

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

    options = ("edit", "add", "namechange", "remove", "transfer", "wto", "help", "exit")
    
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

    elif operation == "remove":

        if len(arguments) != 1:

            error_message = "Invalid command arguments, type help for help."
        
            continue

        if arguments[0] not in scores:

            error_message = "Person does not exist."

            continue

        scores.pop(arguments[0])
        
        send_to_log(f'{datetime.datetime.now()} \| Remove \| {arguments[0]}')

    elif operation == "add":

        if len(arguments) != 1:

            error_message = "Invalid command arguments, type help for help."

            continue

        if arguments[0] == "All":
            
            error_message = "Invalid name."

            continue

        if arguments[0] in scores:

            error_message = "Person already exists."
            
            continue
        
        
        scores[arguments[0]] = 0
        
        send_to_log(f'{datetime.datetime.now()} \| Add \| {arguments[0]}')

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

        send_to_log(f'{datetime.datetime.now()} \| Edit Points \| {arguments[0]} \| Change: {pretty_num(arguments[1])} \| "{arguments[2]}"')

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

        send_to_log(f'{datetime.datetime.now()} \| Points Transfer \| {arguments[0]} to {arguments[1]} \| Amount: {pretty_num(arguments[2])} \| "{arguments[3]}"')

    elif operation == "namechange":

        if len(arguments) != 2:

            error_message = "Invalid command arguments, type help for help."
        
            continue

        if arguments[0] not in scores:
            
            error_message = "Person does not exist."

            continue

        if arguments[1] in scores:

            error_message = "Person already exists."

            continue

        scores[arguments[1]] = scores[arguments[0]]
        scores.pop(arguments[0])

        send_to_log(f'{datetime.datetime.now()} \| Name Change \| {arguments[0]} \| Changed To: {arguments[1]}')

    elif operation == "wto":

        exchange_rate = 10

        if len(arguments != 2):

            error_message = "Invalid command arguments, type help for help."

            continue

        if arguments[0] not in scores and arguments[0] != "All":

            error_message = "Person does not exist."

            continue

        try:

            arguments[1] = int(arguments[1].strip())

        except ValueError:

            error_message = "Input integer for points exchange"

            continue

        wheel_points_file = better_open('./wheel/store.txt', 'r')

        wheel_scores = ast.literal_eval(wheel_points_file.read())

        scores[arguments[0]] += arguments[1]

        wheel_scores[arguments[0]] -= arguments[1] * exchange_rate

        send_to_log(f'{datetime.datetime.now()} \| Wheel Exchange \| {arguments[0]} \| {arguments[1]} for {arguments[1] * exchange_rate}')
        


    elif operation == "help":

        print('\nOperation: edit , Syntax: edit "name" increment "reason" , Description: Edit points of existing people.')
        print('Operation: add , Syntax: add "name" , Description: Add people to leaderboards.')
        print('Operation: namechange , Syntax: namechange "old name" "new name" , Description: Edit names of existing people.')
        print('Operation: remove , Syntax: remove "name" , Description: Remove people from leaderboards.')
        print('Operation: transfer , Syntax: transfer "sender" "recipient" amount "reason" , Description: Transfer points between people.')
        print('Operation: help , Syntax: help , Description: Access this help message.')
        print('Operation: exit , Syntax: exit , Description: Exit the program.\n')

        os.system("pause")

os.system("echo exit | python3 -m wheel.wheel_points_client")
os.system("clear")

output(scores)

save(scores)

store.close()