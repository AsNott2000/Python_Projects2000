import random
import time


def hangman():
    words = [
        "apple",
        "banana",
        "december",
        "istanbul",
        "ferrari",
        "skyfall"
    ]
    word = random.choice(words)
    guessed_letters = []
    attempts = 5

    while attempts > 0:
        print("\nAttempts Left: ", attempts)
        hidden_word = ""
        for letter in word:
            if letter in guessed_letters:
                hidden_word += letter + ""
            else:
                hidden_word += "_"
        print(hidden_word)

        if hidden_word == word:
            print("Congratulations! You guessed the word:", word)
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You have already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct Guess!")
        else:
            print("Wrong Guess!")
            attempts -= 1

    if attempts == 0:
        print("You Lose the Game! The Word Was: ", word)


# Run the Hangman game
print("Hello! Welcome to the Hangman Game. Enjoy!")
time.sleep(3)
print("Let's play Hangman!")
hangman()