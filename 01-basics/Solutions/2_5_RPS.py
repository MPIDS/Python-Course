#!/usr/bin/python
from random import choice

# Rock Paper Scissors

choices = ('r','p','s')
while 1:
    userchoice = raw_input("One, two, three... (type your choice: (r)ock,(p)aper,(s)cissors - any other key to end the game)\n")
    if not userchoice in choices:
        print "Game over."
        break
    else:
        compchoice = choice(choices)
        print "Computer plays: " + compchoice
        if userchoice == compchoice:
            print "Again.\n"
        # note that due to shift symmetry of game rules one can avoid many if-statements
        # a choice defeats its previous and is defeated by its followers
        elif compchoice == choices[(choices.index(userchoice)+1)%3]:
            print "I win!\n"
        else:
            print "Okay, you win.\n"

    
# Rock Paper Scissors Lizard Spock

choices = ('r','k','p','l','s')
while 1:
    userchoice = raw_input("One, two, three... (type your choice: (r)ock,(p)aper,(s)cissors,(l)izard,spoc(k) - any other key to end the game)\n")
    if not userchoice in choices:
        print "Game over."
        break
    else:
        compchoice = choice(choices)
        print "Computer plays: " + compchoice
        if userchoice == compchoice:
            print "Again.\n"
        # note that due to shift symmetry of game rules one can avoid many if-statements
        # a choice defeats its two previous and is defeated by the two followers
        elif compchoice in (choices[(choices.index(userchoice)+1)%5], choices[(choices.index(userchoice)+2)%5]):
            print "I win!\n"
        else:
            print "Okay, you win.\n"

    
