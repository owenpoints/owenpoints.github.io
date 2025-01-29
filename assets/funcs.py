import random

def pretty_num(num):

    if num == int(num):

        num = int(num)

    out = f'{num:,}'
    
    return out

def better_open(filename, mode, codec = "utf-8"):
    
    return open(filename, mode, encoding = codec)

def pretty_dict(dictionary):

    for key, value in dictionary.items():

        if value == int(value):
            
            dictionary[key] = int(value)

    return dictionary

def quick_spin(spins):
    outcomes = [-1, -1, -1, 3, 7, 8, 10, 15, 20]

    total = 0
    for i in range(spins):
        total += random.choice(outcomes)

    return total
