import random

words = ["vehicles", "mississippi", "gorgeous", "building", "husband", "sleeping", "saturday", "administration"]
letters = ""
lives = 4
wrong_letters = []
chosen_word = random.choice(words)
print(f"\n\tThe word has {len(chosen_word)} letters\n")

while lives >= 0:
    guess = input("\nChose a letter: \n")
    if guess in chosen_word:
        print(f"\nCorrect!\n")
    else:
        print(f"\nWrong letter! You have {lives} live(s) to go! \n")
        wrong_letters.append(guess)
        print(wrong_letters)
        lives -= 1

    letters += guess
    letter_count = 0
    for letter in chosen_word:
        if letter in letters:
            print(f"{letter}", end="")
        else:
            print("_", end="")
            letter_count += 1
    if letter_count == 0:
        print(f"\n\tCongrats you WON! The word was {chosen_word}\n")
        break
else:
    print("\nTry again")