def showList(lst):
    '''prints list elements in separate lines'''
    for i, item in enumerate(lst, 1):
        print(f"{i} - {item.strip()}")


def readList(filePath = "todo.txt"):        # param=xyz is a default parameter value
    '''opens file in read mode for show function'''
    with open(filePath, 'r') as file:
        todos = file.readlines()
    return todos


def writeList(todos, filePath = "todo.txt"):
    '''opens file in write mode for edit and delete'''
    with open(filePath, 'w') as file:
        file.writelines(todos)

#
# print(_name_)
#
# if _name_ == '_main_':
#     print(help(showList))
#     print('hello world')