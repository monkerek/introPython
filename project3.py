# http://www.codeskulptor.org/#user30_wHYnTEWGVC_19.py
# =============






import simplegui
# define global variables
time = 0
x = 0
y = 0
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    hr = t / 600
    t -= hr * 600
    mini = t / 100
    t -= mini * 100
    sec = t / 10
    tsec = t - sec * 10
    result =  str(hr) + ':' + str(mini) + str(sec) + '.' + str(tsec)
    return result
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    timer.start()

    
def stop_handler():
    global x, y
    if timer.is_running() == True:
        if time % 10 == 0:
            x += 1
        y += 1
    timer.stop()
    
def reset_handler():
    global time, x, y
    timer.stop()
    time = 0
    x = 0
    y = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time += 1

# define draw handler
def draw_handler(canvas):
    global time
    canvas.draw_text(format(time), (50, 120), 50, 'White')
    canvas.draw_text(str(x) + '/' + str(y),(150,50),30,'Red')

# create frame
frame = simplegui.create_frame('Testing', 200, 150)
timer = simplegui.create_timer(100, timer_handler)
# register event handlers
frame.set_draw_handler(draw_handler)
frame.add_button('Start', start_handler)
frame.add_button('Stop', stop_handler)
frame.add_button('Reset', reset_handler)

# start frame
frame.start()
