import random

def choose_word():
    words = ["apple", "banana", "orange", "grape", "watermelon"]
    return random.choice(words)

def play_game():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to the Word Guessing Game!")
    print("I'm thinking of a fruit. Can you guess it?")

    while True:
        hidden_word = ""
        for letter in word:
            if letter in guessed_letters:
                hidden_word += letter
            else:
                hidden_word += "_"

        print(f"Current word: {hidden_word}")
        print(f"Attempts remaining: {attempts}")

        if hidden_word == word:
            print("Congratulations! You guessed the word!")
            break

        if attempts == 0:
            print(f"Game over! The word was {word}. Better luck next time!")
            break

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")

        elif guess in word:
            print("Correct guess!")
            guessed_letters.append(guess)

        else:
            print("Wrong guess!")
            attempts -= 1

        print("--------------------")

play_game()