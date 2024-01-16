import random

def result(user_choice,computer_choice,user_score,computer_score):
    
    if user_choice == computer_choice:
        computer_score += 1
        user_score += 1
        feedback = "Draw, let's have another"
        
    elif user_choice == "Rock" and computer_choice == "Scissor":
        user_score += 1
        feedback ="you won"
        
    elif user_choice == "Paper" and computer_choice == "Rock":
        user_score += 1
        feedback ="you won"
        
    elif user_choice == "Scissor" and computer_choice == "Paper":
        user_score += 1
        feedback = "you won"
        
    else:
        computer_score += 1
        feedback = "Computer won"
    
    return feedback , user_score, computer_score

#initialization
print("Welcome to rock paper scissor game\n")
option = ["Rock","Paper","Scissor"]
user_score = 0
computer_score = 0
    
# Main program
play_again =  1
while True:
    user_choice = input("Enter Rock or Paper or Scissor: ")
    computer_choice = random.choice(option)
    print(f"Computer choice: {computer_choice}")
    feedback , user_score, computer_score = result(user_choice,computer_choice,user_score,computer_score)
    print(feedback)
    
    print()
    play_again = int(input("Enter 1 to play again or 0 to exit: "))
    if play_again == 0:
        break
    
#Result announcment
print("\nResult\n")    
print(f"User score: {user_score}")
print(f"Computer score: {computer_score}")
input("Press any button to exit")
