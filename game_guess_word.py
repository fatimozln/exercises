import random

words = ["ali", "mahdi", "fati", "sara", "mona"]
print("Guess which of these names(ali, mahdi, fati,sara,mona)")

name = random.choice(words)


def random_name():
    for i in range(0, len(name)):
        print("_", end=" ")
    return


print("\nThe word you have to guess:")
print(random_name())

a = 0
while a < 3:
    guess = input("your guess:")
    if guess == name:
        print("wine :)")
        break
    else:
        print("lose: (")

    a += 1

else:
    print("...the current name=", name)
