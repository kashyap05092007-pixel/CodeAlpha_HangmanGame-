import random

# List of 5 predefined words
words = ["apple", "tiger", "table", "robot", "chair"]

# Randomly choose a word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum wrong attempts
attempts = 6

print("🎮 Welcome to Hangman Game!")

# Game loop
while attempts > 0:

    # Display word
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check win condition
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word.")
        break

    # User input
    guess = input("Enter a letter: ").lower()

    # Check guess
    if guess in word:
        if guess not in guessed_letters:
            guessed_letters.append(guess)
            print("✅ Correct Guess!")
        else:
            print("⚠ You already guessed that letter.")

    else:
        attempts -= 1
        print("❌ Wrong Guess!")
        print("Remaining Attempts:", attempts)

# Lose condition
if attempts == 0:
    print("\n💀 Game Over!")
    print("The word was:", word)
