
shoping_list = []

while True:
    item = input("enter your item:")
    if not item == "done":
        shoping_list.append(item)
    else:
        break

print("your list:", shoping_list)
