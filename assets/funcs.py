def pretty_num(num):

    if num == int(num):

        num = int(num)

    out = f'{num:,}'
    
    return out

def better_open(filename, mode, codec = "utf-8"):
    
    return open(filename, mode, encoding = codec)
