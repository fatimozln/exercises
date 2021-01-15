import random

words = ['ali', 'mahdi', 'fati', 'sara', 'mona']
print("Guess which of these names  (  ali  ,  mahdi  ,  fati  ,  sara  ,  mona  )")
random_word = random.choice(words)

right_guess = []
Wrong_guess = []


while len(Wrong_guess) < 5 and len(right_guess) != len(random_word):
    for letter in random_word:
        if letter in right_guess:
            print(letter, end=' ')
        else:
            print("_", end=' ')

    print("\n")
    print("Number of false guesses {}/5".format(len(Wrong_guess)))
    print("\n")
    guess = input("Guess a letter :")

    if len(guess) > 1:
        print("Please enter a letter")
        continue

    if not guess.isalpha():
        print("Please enter a letter!")

    if guess in Wrong_guess or right_guess:
        print("You have already entered this letter")

    if guess in random_word:
        right_guess.append(guess)
        if len(right_guess) == len(random_word):
            print("YOU WINE  :)")
            break
    else:
        Wrong_guess.append(guess)

else:
    print("YOU LOSE  :(   ...   The right word IS", random_word)
