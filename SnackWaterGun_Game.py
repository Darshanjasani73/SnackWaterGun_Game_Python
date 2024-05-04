import random

def game(comp,player):
    if  comp == 's':
        if player == 'w':
            return False
        elif player == 'g':
            return True
    elif comp == 'w':
        if comp == 'g':
            return False
        elif comp == 's':
            return True
    elif comp == 'g':
        if player == 's':
            return False
        elif player == 'w':
            return True
    elif comp == player:
        return None
print("comp's turn: snack(s) water(w) gun(g)?")
RandNo = random.randint(1,3)


if RandNo == 1:
    comp = 's'
elif RandNo == 2:
    comp = 'w'
elif RandNo == 3:
    comp = 'g'
player = input("player's turn: snack(s) water(w) gun(g)?  ")
result = game(comp, player)

print(f"computer choose {comp}")
print(f"player choose {player}")
if result == None:
    print("The game is tie!!!")
elif result:
    print("player is win!!!")
else:
    print("player is lose")
















