from random import randint
EASY_TURNS=10
HARD_TURNS=5
def check(user_guess,actual_answer,turns):
    if(user_guess>actual_answer):
        print("too high")
        return turns-1
    elif(user_guess<actual_answer):
        print("too low")
        return turns-1
    else:
        print("you have got it")
def choose_level():
    level=input("choose a difficulty. type 'easy' or 'hard':")
    if(level=='easy'):
        return EASY_TURNS
    else:
        return HARD_TURNS
def game():
    print("welcome tothe number guessing game! ")
    print("I am thinking of a number between 1 and 100")
    ans=randint(1,100)
    print(f"the actual answer is: {ans}")
    turns=choose_level()
    guess=0
    while(guess!=ans):
        print(f"you have {turns} attempts remaining to guess the number")
        guess=int(input("make guess:"))
        turns=check(guess,ans,turns)
        if turns==0:
            print("you lose")
            return
        elif(guess!=ans):
            print("guess again")
   
game()




    
    