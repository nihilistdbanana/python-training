#Guess the number game using python
import random
randno=random.randint(1,10)
guesses=0
num=None
while (num!=randno):       
    num=int(input("guess a number: "))
    guesses+=1
    if num>randno:
        print("Lower number please")
    elif num<randno:
        print("Higher number please")
    else:
        print(f"CORRECT!\n The number of guesses you used to arrive this number={guesses}")
