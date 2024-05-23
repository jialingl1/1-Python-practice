computer_choice = "scissors"
user_choice = input("Please select rock, paper or scissors\n")

if computer_choice == user_choice:
    print("tie")
elif user_choice == "rock" and computer_choice == "scissors":
    print("win")
elif user_choice == "paper" and computer_choice == "rock":
    print("win")
elif user_choice == "scissors" and computer_choice == "paper":
    print("win")
else:
    print("you lose")