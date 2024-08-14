import random

def game(Comp,Player):
    if Comp == Player:
        print("DRAW")
    elif Comp == 'r':
        if Player == 'p':
            print("PLAYER WON")
        elif Player == 's':
            print("COMP WON")
    elif Comp == 'p':
        if Player == 's':
            print("PLAYER WON")
        elif Player == 'r':
            print("COMP WON")
    elif Comp == 's':
        if Player == 'r':
            print("PLAYER WON")
        elif Player == 'p':
            print("COMP WON")
    
print("Comp turn: Rock(r) , Paper(p) or Scissor(s)")
rand = random.randint(1, 3)
if rand == 1:
    Comp = 'r'
elif rand == 2:
    Comp = 'p'
elif rand == 3:
    Comp = 's'
    
Player = input("Player turn: Rock(r) , Paper(p) or Scissor(s)")

print(f"Computer chose {Comp}")
print(f"Player  chose {Player}")
 
game(Comp,Player)
    
