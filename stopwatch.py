# template for "Stopwatch: The Game"
import simplegui
# define global variables
tens_of_second = 0
x = 0
y = 0

# define helper function format that converts integer
# counting tenths of seconds into formatted string A:BC.D
def format(t):
    D = t%10
    C = (t//10) % 60%10
    B = (t//10)%60//10
    A = (t//10)//60
    digits_show = str(A) + ':' + str(B)+str(C) + '.' + str(D)
    return digits_show
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def button_reset():
    timer.stop()
    global tens_of_second
    tens_of_second = 0
    format (tens_of_second)
    global x
    global y
    x = 0
    y = 0
    
    
def button_start():
    global tens_of_second
    format (tens_of_second)
    timer.start()
    
def button_stop():
    timer.stop()
    global tens_of_second
    format (tens_of_second)
    global x
    global y
    x +=1
    if tens_of_second%10 ==0:
        y +=1
    
        
def draw(canvas):
    global x
    global y
    global tens_of_second
    canvas.draw_text(str(str(y)+"/"+str(x)), [10,30], 26, "green")
    canvas.draw_text(format(tens_of_second), [120,100], 36, "White")
   
    



# define event handler for timer with 0.1 sec interval
def timer_handler():
    global tens_of_second
    tens_of_second = tens_of_second + 1
    
   
   
# create frame
frame = simplegui.create_frame('stopwatch', 300,200)

# register event handlerson
button_start = frame.add_button('Start', button_start, 50)
button_stop = frame.add_button('Stop', button_stop, 50)
button_reset = frame.add_button('Reset', button_reset, 50)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, timer_handler)

# start timer and frame
frame.start()
timer.start()


# remember to review the grading rubric