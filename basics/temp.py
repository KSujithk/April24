import random
random_number = random.randint(1,100)
did_user_win = False
for chance in range(6,0,-1):
    guessed_number = int(input("Enter your number: "))
    if guessed_number == random_number:
        print("Hooray!... You have won")
        did_user_win = True
        break
    elif guessed_number > random_number:
        print("Actual number is little bit lower than what you have guessed")
    else:
        print("Actual number is little bit higher than what you have guessed")
    print(f"you have {chance-1} more chances")
if not did_user_win:
    print(" Bad luck try again.  ")