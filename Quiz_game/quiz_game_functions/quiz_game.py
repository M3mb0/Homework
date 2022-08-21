questions = {
    "\nWhich is the capital of China?\n": "C",
    "\nWhich is the biggest freshwater lake in the world?\n": "C",
    "\nWhich is the longest river in the world?\n": "A",
    "\nWhich is the highest mountain from Europe?\n": "C",
    "\nHow hot is surface of the sun?\n": "B"
}

options = [["A. Hong Kong", "B. Shanghai", "C. Beijing"],
           ["A. Lake Victoria", "B. Lake Baikal", "C. Lake Superior"],
           ["A. Nile", "B. Amazon", "C. Mississippi"],
           ["A. Mount Everest", "B. Mont Blanc", "C. Mount Elbrus"],
           ["A. 10000 Celsius", "B. 5600 Celsius", "C. 2349000 Celsius"]]


def quiz_game():
    print("\n\tLet's start the quiz game\n")
    print("For each correct answer you will get 1 point\n")
    check_leaderboard()
    player_names = []
    i = 1
    while True:
        try:
            player_no = int(input("How many players?: "))
            break
        except ValueError:
            print("Please enter a number")
    while i <= player_no:
        player_name = input(f"Please add player {i} name: ")
        player_names.append(player_name)
        i += 1
    for player in player_names:
        print(f"Player {player} turn")
        score = 0
        question_num = 0
        guesses = []
        for x in questions:
            print(x)
            for j in options[question_num]:
                print(j)
            guess = input("\nEnter (A,B or C): \n")
            guess = guess.upper()
            guesses.append(guess)
            question_num += 1
            score += int(check_answer(questions.get(x), guess))
            print(f"\nYour score is {score} points\n")
            print(f"Your answers are: {guesses}")

        file = open("score.txt", "a")
        file.write(str(f"Name: {player}, Score: {score}\n "))
        file.close()


def check_answer(answer, guess):
    if answer == guess:
        print("Correct")
        return 1
    else:
        print("Wrong")
        return 0


def check_leaderboard():
    user_input = input("\nDo you want to check leaderboard? Y/N\n")
    user_input = user_input.upper()

    if user_input == "Y":
        file = open("score.txt", "r")
        for line in file:
            print(line)
        file.close()
    else:
        return False
