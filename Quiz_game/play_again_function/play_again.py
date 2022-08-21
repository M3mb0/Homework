def play_again():
    user_answer = input("\nDo you want to play again? Y/N\n")
    user_answer = user_answer.upper()

    if user_answer == 'Y':
        return True
    else:
        return False
