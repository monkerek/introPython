# Rock-paper-scissors-lizard-Spock 
# by Dong Chen from China

#import random module
import random

# convert name to number
def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print "Invalid input!"

# convert number to a name
def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print "Invalid input!"
    

def rpsls(player_choice): 
    # print out the messages for choices
    print ""
    print "Player chooses",player_choice
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0,4)
    comp_choice = number_to_name(comp_number)
    print "Computer chooses",comp_choice
    
    # compute difference of comp_number and player_number modulo five
    difference = (comp_number - player_number) % 5

    #print winner message
    if difference == 1 or difference == 2:
        print "Computer wins!"
    elif difference == 3 or difference == 4:
        print "Player wins!"
    else:
        print "Player and computer tie!"

    
# test your code - LEAVE THESE CALLS IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
