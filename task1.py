import random

def play_hangman():
    words = ["python", "hangman", "computer", "science", "keyboard"]
    word = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")

    while incorrect_guesses < max_incorrect:
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord: " + display_word)
        print(f"Incorrect guesses: {incorrect_guesses}/{max_incorrect}")
        print("Guessed letters:", ", ".join(guessed_letters) if guessed_letters else "None")

        if "_" not in display_word:
            print("\nCongratulations! You guessed the word:", word)
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Wrong guess! '{guess}' is not in the word.")

    if incorrect_guesses == max_incorrect:
        print("\nGame Over! You've used all your incorrect guesses.")
        print("The word was:", word)


if __name__ == "__main__":
    play_hangman()