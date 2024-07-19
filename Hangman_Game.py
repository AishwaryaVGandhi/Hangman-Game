import random
import Hangman_Stages

dictionary = ["sunflower", "jasmine", "bougainvillea", "lavender", "chamomile", "marigold", "hibiscus"]
life = 7

print("Welcome to Hangman Game !!")

word = random.choice(dictionary)
length = len(word)
display = ["_"] * length
guess_list = []

print(" ".join(display))

game_over = False
while not game_over:
    guess = input("\nGuess a letter : ").strip().lower()

    if guess in guess_list:
        print(f"You have already guessed {guess}. Try Again !!")
        continue
    guess_list.append(guess)

    if guess in word:
        for position in range(len(word)):
            if guess == word[position]:
                display[position] = guess
        print(" ".join(display))
        print("Correct Guess !!")

    else:
        life -= 1
        print(Hangman_Stages.stages[life])
        print(f"Wrong guess !! You have {life} lives left.")

    if life == 0:
        print("Game Over !! You Lost !!")
        print(f"The word was: {word}.")
        game_over = True

    if "_" not in display:
        print("You Won !!")
        game_over = True
