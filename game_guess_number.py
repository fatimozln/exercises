
import random
current_number = random.randint(1, 10)
print(current_number)


def run_game():
    a = 0
    while a < 5:
        try:
            guess = int(input("Guess a number between 1 and 10:"))
        except ValueError:
            print("your inpute not number")
        else:
            if guess == current_number:
                print("wine!the current number is", current_number)
                break
            else:
                print("lost!")

            a += 1

    else:
        print("You could not guess correctly. Correct number =", current_number)


run_game()
