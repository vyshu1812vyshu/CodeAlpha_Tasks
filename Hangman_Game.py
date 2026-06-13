import random

# Predefined list of words
words = ["python", "apple", "banana", "computer", "flower"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum incorrect guesses
incorrect_guesses = 0
max_attempts = 3

print("🎮 Welcome to Hangman Game!")

while incorrect_guesses < max_attempts:

    # Display the word with underscores
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if player has guessed the word
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    # Take user input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single alphabet letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess in word:
        print("✅ Correct guess!")
    else:
        incorrect_guesses += 1
        print("❌ Wrong guess!")
        print("Remaining attempts:", max_attempts - incorrect_guesses)

# If player loses
if incorrect_guesses == max_attempts:
    print("\n💀 Game Over!")
    print("The word was:", word)