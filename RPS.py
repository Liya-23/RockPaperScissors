import random

options_provided = 'RPS'

def get_playerinput():
    playerinput = None
    while playerinput is None: 
        playerinput = input("Choose: \n(R) ➡ Rock  \t(P) ➡ Paper \t(S) ➡ Scissors \n\nChoose: ")
        if playerinput.upper() not in options_provided:
            playerinput = None
    return playerinput.upper()        

def get_compinput():
    compinput = random.randint(0,2)
    compinput = options_provided[compinput]
    return compinput.upper()

def check_for_ties(playerinput,compinput):
    if playerinput == compinput:
        return True

def see_who_won(playerinput,compinput):
    if compinput == "R" and playerinput == "S":
        print("Comp wins!")
    elif compinput == "S" and playerinput == "P":
        print("Comp wins!")
    elif compinput == "P" and playerinput == "R":
        print("Comp wins!")        
    else:
        print("Player wins!")
        print('%s beats %s' % (playerinput, compinput))
        
def play_game():
    playerinput = get_playerinput()
    compinput = get_compinput()
    if check_for_ties(playerinput,compinput):   
        print("its a tie, both players picked %s: " % playerinput)
    else:
        print("Computer picked: %s" % compinput)
        print("Player picked: %s" % playerinput)
        see_who_won(playerinput, compinput)     
        
if __name__ == "__main__":
    play_game()        