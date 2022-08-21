import random

start_no = 1
end_no = 10
chosen_number = random.randint(start_no, end_no)

print("\n\tYou have only 3 chances to guess the number!\n")
count = 0
while count < 3:
    count += 1
    guess = int(input("Guess the number: "))

    if chosen_number == guess:
        print("You found the number after", count, "try(s)")
        break
    elif chosen_number > guess:
        print("The number is bigger1")
    elif chosen_number < guess:
        print("The number is smaller!")
if count >= 3:
    print("\n\tBetter luck next time\n")
