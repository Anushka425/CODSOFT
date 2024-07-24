import random

user_score=0
computer_score=0

print("Rock,Paper,Scissor Game:score/5 \n")
while True:
    while user_score<3 and computer_score<3:
        user=input("Enter a choice from: rock/paper/scissor- ").lower()
        while user not in ['rock','paper','scissor']:
            user=input("Enter a choice from: rock/paper/scissor- ").lower()
        computer=random.choice(['rock','paper','scissor'])
        print("Computer chose",computer)
        print("Player chose",user)
        if user=='scissor' and computer=='paper':
            user_score+=1
        elif user=='paper' and computer=='rock':
            user_score+=1
        elif user=='rock' and computer=='scissor':
            user_score+=1
        elif computer=='scissor' and user=='paper':
            computer_score+=1
        elif computer=='paper' and user=='rock':
            computer_score+=1
        elif computer=='rock' and user=='scissor':
            computer_score+=1 
        else:
            print("It's a tie")
        print("Player score:",user_score)
        print("Computer score:",computer_score)
    
    if user_score>computer_score:
        print("YOU WINS!!")
    else:
        print("COMPUTER WIN!!")

    choice=input("Do you want to play again : y/Y for YES")
    if not(choice=='y' or choice=='Y'):
        break;
    user_score=0
    computer_score=0

        