
def inqueue(item):
    q.append(item)
    return


def dequeue():
    s = q[0]
    del(q[0])
    return s


q = []

for i in range(0, 3):
    item = input("item:")
    inqueue(item)

print(dequeue())
print(dequeue())
print(dequeue())
