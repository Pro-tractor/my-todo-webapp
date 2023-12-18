import time

FILEPATH = "todos.txt"


def read_file(filepath=FILEPATH):
    # CONTEXT MANAGER - Reads file and stores lines in list
    with open(filepath, "r") as txt_file:
        todoList = txt_file.readlines()
    return todoList


def write_file(aList, filepath=FILEPATH):
    with open(filepath, "w") as txt_file:
        txt_file.writelines(aList)


def numerate_list(a_list):
    for index, item in enumerate(a_list):
        strippedItem = item.strip('\n')  # Strips the extra space in between each item
        print(f"{index + 1}. {strippedItem}")


def current_date_time():
    now = time.strftime("%B %d %Y  %I:%M %p")
    print(now)
