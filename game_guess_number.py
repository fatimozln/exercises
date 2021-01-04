
import random
#current_number = random.randint(1, 10)


def run_game():
    a = 0
    guess = 0
    current_number = random.randint(1, 10)
    while a < 5:
        try:
            guess = int(input("Guess a number between 1 and 10:"))
        except ValueError:
            print("your inpute not number")
        else:
            if guess == current_number:
                print("wine!the current number is", current_number)
                break

            elif guess > current_number:
                print("A number smaller than", guess)

            elif guess < current_number:
                print("A number higher than", guess)

            else:
                print("lost!")

            a += 1

    else:
        print("You could not guess correctly. Correct number =", current_number)

    again = input("Do you want to play again?[yes/no]")
    if again.lower() == "yes":
        run_game()
    else:
        print("  goodbye  :)")


run_game()
