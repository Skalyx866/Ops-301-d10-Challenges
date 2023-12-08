#!/usr/bin/env python3

# importing random library
import random

# declare variables)
hand = random.randrange(1, 3)
# defining function
def which_hand(hand):
    print("Which hand has the prize, left or right?")
    if hand == 1:
        print("The left hand had it!")
    elif hand ==2:
        print ("The right hand had it!")
    else:
        print("Both hands had it!")

which_hand(hand)
