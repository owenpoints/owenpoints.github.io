import ast
from decimal import Decimal

def pretty_num(num):
    if num == int(num):
        num = int(num)

    result = f'{num:,}'
    
    return result

def better_open(filename, mode, codec = "utf-8"):
    return open(filename, mode, encoding = codec)

def import_scores(path):
    with better_open(path, 'r') as score_file:
        result = ast.literal_eval(score_file.read())

    result = {name: Decimal(result[name]) for name in result}

    return result

def sort_scores(scores):
    scores = dict(sorted(scores.items(), key=lambda item: -1 * item[1]))

    return scores

def pretty_dict(dictionary):
    for key, value in dictionary.items():
        if value == int(value):
            dictionary[key] = Decimal(int(value))

    return dictionary

def format_scores(scores):
    scores = sort_scores(scores)

    scores = pretty_dict(scores)

    return scores

def save(scores, path):
    scores = {name: str(scores[name]) for name in scores}

    with better_open(path, 'w') as scores_file:
        scores_file.write(str(scores))
