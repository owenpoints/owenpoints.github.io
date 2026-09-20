import os
import datetime
from assets.funcs import pretty_num, better_open, format_scores, save, import_scores
from wheel.wheel_assets.funcs import wheel_output
from decimal import Decimal

def send_to_log(message):
    with better_open('./points/log.txt', 'r') as log:
        content = log.read()

    with better_open('./points/log.txt', 'w') as log:
        log.write(message + '\n' + content)

def output(scores):
    output_str = "# Global Owen Points Rankings\n\n|Ranking|Name|Owen Points|\n| ----------- | ----------- | ----------- |\n"
    
    scores = dict(sorted(scores.items(), key=lambda item: -1 * item[1]))

    for index, name in enumerate(scores):
        output_str += f"|{index + 1}.|{name}|{pretty_num(scores[name])}|\n"

    output_str += "\n## Report Someone or Request Points [Here](https://docs.google.com/forms/d/e/1FAIpQLScEe4ohzK1m1LlYeYMin0rPYx5sfSNmHLy6EeX2wYl5e1vPCQ/viewform?usp=publish-editor).\n"
    output_str += "\n## !! Those Under -500 Owen Points will be [Executed Live](https://www.twitch.tv/will_of_owen) !!\n"
    output_str += "\n## Top Owen Updates Can be Found [Here](./blog).\n"
    output_str += "\n## Wheel Points Leaderboard can be Found [Here](./wheel)\n"
    output_str += "\n## Previous Seasons can be Found [Here](./seasons)\n"
    output_str += "\n\n## Owen Points Log:\n"

    with better_open('./points/log.txt', 'r') as log:
        lines = log.readlines()

    for line in lines:
        output_str += line + '\n'
    
    with better_open('README.md', 'w') as page:
        page.write(output_str)

scores = import_scores('./points/scores.txt')
wheel_scores = import_scores('./wheel/scores.txt')

error_message = ''

while True:
    os.system("cls")

    scores = format_scores(scores)

    for name, score in scores.items():
        print(f"{name}: {score}")
    
    if error_message:
        print(f"\n!! {error_message} !!\n")

        error_message = ''

    commands = ("edit", "add", "namechange", "remove", "transfer", "ofw", "help", "exit")
    
    raw_command = input(f"Input operation {commands}: ").strip()

    if not raw_command:
        error_message = "Please input a command."
        continue

    operation = raw_command.split()[0].lower()

    arguments = [item.strip() for item in raw_command.split('"')[1:] if item and item != " "]

    if operation == "exit":
        break
 
    if operation not in commands:
        error_message = "Enter valid operation."
        continue

    elif operation == "remove":
        if len(arguments) != 1:
            error_message = "Invalid command arguments, type help for help."
            continue

        name = arguments[0]

        if name not in scores:
            error_message = f"\"{name}\" does not exist."
            continue
        
        scores.pop(name)
        wheel_scores.pop(name)
        
        send_to_log(f'{datetime.datetime.now()} \| Remove \| {name}')

    elif operation == "add":
        if len(arguments) != 1:
            error_message = "Invalid command arguments, type help for help."
            continue

        name = arguments[0]

        if name == "All":
            error_message = "Name cannot be \"All\"."
            continue

        if name in scores:
            error_message = f"\"{name}\" already exists."
            continue
        
        scores[name] = Decimal(0)
        wheel_scores[name] = Decimal(0)

        send_to_log(f'{datetime.datetime.now()} \| Add \| {name}')

    elif operation == "edit":
        if len(arguments) != 3:
            error_message = "Invalid command arguments, type help for help."
            continue

        name = arguments[0]

        if name not in scores and name != "All":
            error_message = f"\"{name}\" does not exist."
            continue

        try:
            amount = Decimal(arguments[1])
        
        except ValueError:
            error_message = "Input float for points increment."
            continue
        
        if name == "All":
            scores = {key: scores[key] + amount for key in scores}

        else:
            scores[name] += amount

        reason = arguments[2]

        send_to_log(f'{datetime.datetime.now()} \| Edit Points \| {name} \| Change: {pretty_num(amount)} \| "{reason}"')

    elif operation == "transfer":
        if len(arguments) != 4:
            error_message = "Invalid command arguments, type help for help."
            continue

        sender_name = arguments[0]
        recipient_name = arguments[1]
        reason = arguments[3]

        if not sender_name in scores and sender_name != "All":
            error_message = f"\"{sender_name}\" does not exist."
            continue

        if not recipient_name in scores and recipient_name != "All":
            error_message = f"\"{recipient_name}\" does not exist."
            continue

        if recipient_name == "All" and sender_name == recipient_name:
            error_message = "All cannot send to All"
            continue

        try:
            amount = Decimal(arguments[2])
        
        except ValueError:
            error_message = "Input float for points transfer."
            continue
        
        if recipient_name == "All":
            scores[sender_name] -= amount * len(scores)
            scores = {key : scores[key] + amount for key in scores}

        elif sender_name == "All":
            amount_per_person = Decimal(round(amount / len(scores)))
            total_to_recipient = amount_per_person * len(scores)

            if amount_per_person == 0:
                error_message = f"Amount rounds to zero ({amount / len(scores)})."

            amount = total_to_recipient

            scores = {key : scores[key] - amount_per_person for key in scores}
            scores[recipient_name] += total_to_recipient

        else:
            scores[sender_name] -= amount
            scores[recipient_name] += amount

        send_to_log(f'{datetime.datetime.now()} \| Points Transfer \| {sender_name} to {recipient_name} \| Amount: {pretty_num(amount)} \| "{reason}"')

    elif operation == "namechange":
        if len(arguments) != 2:
            error_message = "Invalid command arguments, type help for help."
            continue

        old_name = arguments[0]

        if old_name not in scores:
            error_message = f"\"{old_name}\" does not exist."
            continue

        new_name = arguments[1]

        if new_name in scores:
            error_message = f"\"{new_name}\" already exists."
            continue

        scores[new_name] = scores[old_name]
        scores.pop(old_name)

        wheel_scores[new_name] = wheel_scores[old_name]
        wheel_scores.pop(old_name)

        send_to_log(f'{datetime.datetime.now()} \| Name Change \| {old_name} \| Changed To: {new_name}')

    elif operation == "ofw":
        EXCHANGE_RATE = 10

        if len(arguments) != 2:
            error_message = "Invalid command arguments, type help for help."
            continue

        name = arguments[0]

        if name not in scores and name != "All":
            error_message = f"\"{name}\" does not exist."
            continue

        try:
            amount = Decimal(arguments[1])

        except ValueError:
            error_message = "Input float for points exchange"
            continue

        scores[name] += amount

        wheel_scores[name] -= amount * EXCHANGE_RATE

        send_to_log(f'{datetime.datetime.now()} \| Wheel Exchange \| {name} \| {pretty_num(amount)} for {pretty_num(amount * EXCHANGE_RATE)}')
        
    elif operation == "help":
        print('\nOperation: edit , Syntax: edit "name" increment "reason" , Description: Edit points of existing people.')
        print('Operation: add , Syntax: add "name" , Description: Add people to leaderboards.')
        print('Operation: namechange , Syntax: namechange "old name" "new name" , Description: Edit names of existing people.')
        print('Operation: remove , Syntax: remove "name" , Description: Remove people from leaderboards.')
        print('Operation: transfer , Syntax: transfer "sender" "recipient" amount "reason" , Description: Transfer points between people.')
        print('Operation: ofw , Syntax: ofw "name" quantity , Description: Turn wheel points into Owen Points.')
        print('Operation: help , Syntax: help , Description: Access this help message.')
        print('Operation: exit , Syntax: exit , Description: Exit the program.\n')

        os.system("pause")

output(scores)

save(scores, './points/scores.txt')

wheel_output(wheel_scores)

save(wheel_scores, './wheel/scores.txt')
