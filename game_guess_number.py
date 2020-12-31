
import random
current_number = random.randint(0, 10)
print(current_number)

while True:
    guess = int(input("Guess a number between 0 and 10:"))
    if guess == current_number:
        print("wine!")
        break
    else:
        print("lost!")
