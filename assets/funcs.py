def pretty_num(num):

    out = f'{num:,}'
    
    return out

def better_open(filename, mode, codec = "utf-8"):
    
    return open(filename, mode, encoding = codec)

def pretty_dict(dictionary):
    
    for key, value in dictionary.items():
    
        if value == int(value):
    
            dictionary[key] = int(value)
    
    return dictionary
