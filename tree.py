import sys

text = '"DataA": {"name":"One name""Level": "One","Priority": "Highest","SubdataA":{"name":"One nameSubdataA","Level": "One","Priority": "Highest",}}'
length = len(text)
cont = 0
level = 0
tree = {}

def check_validate_index(text, index):
    try:
        text[index]
        return True
    except IndexError:
        return False

def get_node(text, idx, level, depth):
    # print(level)
    node = ""
    index = idx+1
    while (check_validate_index(text, index)) and (text[index] != "{"):
        node += text[index]
        if text[index] == "}" : 
            break 
        index += 1
    if depth in tree:
        tree[depth].append((level, node))
    else:
        tree[depth] = []
        tree[depth].append((level, node))
    # print(tree)
    return index

def format_text(text):
    length = len(text)
    level = 0
    depth = 0
    cont = 0
    while cont < length: 
        if ((check_validate_index(text, cont)) and text[cont] == "}"):
            level -= 1
            if level == 0: depth += 1
                   
        if((check_validate_index(text, cont)) and text[cont] == "{"):
            level += 1
            cont = get_node(text, cont, level, depth)
        else:
            cont += 1
    # print(tree)

def show():
    for key in tree:
        list = tree[key]
        cont = 1
        for tuple in list:
            if cont == 1: print(key)
            print("|___" * cont, tuple)
            cont += 1
        

if __name__ == "__main__":
    text = ""
    if len(sys.argv) > 1:
        if sys.argv[1] == "test":
            text = '"DataA": {"name":"One name""Level": "One","Priority": "Highest","SubdataA":{"name":"One nameSubdataA","Level": "One","Priority": "Highest",}"SubdataA": {"name":"One nameSubdataA2""Level": "Two","Priority": "High","SubdataAA":{"name":"One nameSubdataAA""level": "One","Priority": "Highest",}}}"DataB": {"name":"One nameB""Level": "Two","Priority": "Highest","SubdataB":{"name":"One nameSubdataB""Level": "One","Priority": "Highest",}}'
    else:
        print("Type a object")
        text = input()
    format_text(text)
    show()