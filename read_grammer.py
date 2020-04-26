
file = open("grammer.txt", "r")
grammer = file.read()

def spliter(grammer):
    list = []
    grammer_split = grammer.split("\n")
    for line in grammer_split:
        line_of_grammer = line.split("->")
        list.append(line_of_grammer)

    return list

def create_dic(grammer):
    list_of_grammer = spliter(grammer)
    grammer_dic = {}

    for line in list_of_grammer:
        
        key = line[0]
        tmep = line[1]
        temp = tmep.split('|')
        
        grammer_dic[key] = temp
        
    return grammer_dic


if __name__ == "__main__":
    # print(create_dic(grammer))
    create_dic(grammer)