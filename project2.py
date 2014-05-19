# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

# initialize global variables used in your code
num_range = 100
remaining_guess = 7
num_generated = random.randint(0, num_range)

# helper function to start and restart the game
def new_game():
    print ""
    global num_range
    global remaining_guess
    global num_generated
    num_generated = random.randint(0, num_range)
    if num_range == 100:
        remaining_guess = 7
    else:
        remaining_guess = 10
    print "New game. Range is from 0 to",num_range    
    print "Number of remaining guesses is",remaining_guess


# define event handlers for control panel
def range100():
    global num_range
    num_range = 100
    new_game()

def range1000():
    global num_range
    num_range = 1000
    new_game()
    
def input_guess(guess):
    print 
    print "Guess was",guess
    global remaining_guess
    global num_generated
    remaining_guess -= 1
    print "Number of remaining guesses is",remaining_guess
    store = int(guess)
    if store == num_generated:
        print "Correct!"
        new_game()
    else:
        if remaining_guess == 0:
            print "You ran out of guesses. The number was",num_generated
            new_game()
        else:
            if num_generated > store:
                print "Higher!"
            else:
                print "Lower!"
    
# create frame
f = simplegui.create_frame("Guess the number",200,200)


# register event handlers for control elements
f.add_button("Range is (0,100)",range100,200)
f.add_button("Range is (0,1000)",range1000,200)
f.add_input("Enter a guess",input_guess,200)

# call new_game and start frame
new_game()
