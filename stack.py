
def push(item):
    q.append(item)
    return


def pop():
    last_element = len(q)-1
    s = q[last_element]
    del(q[last_element])
    return s


q = []

for i in range(0, 3):
    item = input("item:")
    push(item)


for i in range(0, len(q)):
    print(pop())
