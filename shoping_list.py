
shoping_list = []

print("please enter your requirements =")


def show_help():
    print("""
    enter <done> to stop add list
    enter <show> to shoe your list
    """)


def show_list():
    print("your list:", shoping_list)


while True:
    item = input("enter your item:")

    if item == "done":
        break

    elif item == "show":
        show_list()

    elif item == "help":
        show_help()

    elif not item in shoping_list:
        shoping_list.append(item)

show_list()
