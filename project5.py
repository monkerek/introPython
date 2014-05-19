# implementation of card game - Memory

import simplegui
import random
Turns = 0
prev_index1 = -1
prev_index2 = -1
# helper function to initialize globals
def new_game():
    global state, Turns, label, label1
    state = 0
    
    global lis, exposed
    lis = [num for num in range(8)]
    lis = lis + lis
    random.shuffle(lis)
    
    exposed = [False for num in range(16)]
    
    Turns = 0
    label.set_text("Turns = " + str(Turns))
    label1.set_text("")
    
# define event handlers
def mouseclick(pos):
    global state, Turns, label, prev_index1, prev_index2
    if prev_index1 >= 0 and prev_index2 >= 0:
        exposed[prev_index1] = False
        exposed[prev_index2] = False
        prev_index1 = -1
        prev_index2 = -1
    
    index = pos[0] / 50 * 4 + pos[1] / 50
    if not exposed[index]:
        if state == 0:
            state = 1
        elif state == 1:
            state = 2
        else:
            state = 1
 
        exposed[index] = True
        
        if state == 1:
            prev_index1 = index
        else:
            Turns += 1
            label.set_text("Turns = " + str(Turns))
            if lis[prev_index1] == lis[index]:
                prev_index1 = -1
                prev_index2 = -1
            else:
                prev_index2 = index
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global label1
    win = True
    for row in range(0, 200, 50):
        for column in range(0, 200, 50):
            ind = row / 50 * 4 + column / 50
            if exposed[ind]:
                canvas.draw_polygon([(row, column), (row, column + 49),(row + 49, column + 49),(row + 49, column)], 1, 'Yellow', 'Yellow')
                canvas.draw_text(str(lis[ind]), (row + 17, column + 34), 30, 'Blue')
            else:
                win = False
    
    if win:
        label1.set_text('Congratulations!')

    for	index in range(0, 200, 50):
        canvas.draw_line((index, 0), (index, 200), 2, 'Blue')
        canvas.draw_line((0, index), (200, index), 2, 'Blue')
            

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 200, 200)
frame.set_canvas_background("Red")
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = " + str(Turns))
label1 = frame.add_label("")
# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
