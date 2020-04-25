from . import tokenizer

def filter(str):
    new_str = str.replace('<', '')
    new_str = new_str.replace('>', '')
    new_str = new_str.replace(' ', '')
    new_str = new_str.replace('\n', '')
    return new_str

def spliter(str):
    str = filter(str)
    colon_split = str.split(":")
    return colon_split

def reader():
    file = open("TestCase1.txt", "r")
    tokens = []
    for line in file:
        data = spliter(line)
        token = tokenizer.Token(data[0], data[1])
        tokens.append(token)

    return tokens