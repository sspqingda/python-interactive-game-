# implementation of card game - Memory
import simplegui
import random

card_number = range(16)
exposed = []
pair_position = []
pair_value = []
moves = 0
state = 0
# helper function to initialize globals
def init():
    global state, card_number,exposed, moves
    random.shuffle(card_number)
    exposed = []
    moves = 0
    l.set_text("Moves="+str(moves))
    state = 0
    for i in range(16):
        card_number[i] = card_number[i]%8
        exposed.append(False)
     
# define event handlers
def mouseclick(pos):
    global state, moves,exposed,card_number
    global pair_position,pair_value
    
    for i in range(16):
        if i*50 <=pos[0]<(i+1)*50:
            if exposed[i]== True:
                return
            else:
                exposed[i] = True
                position = i
                value = card_number[i]
    
    if state == 0:
        state = 1
        pair_position.append(position)
        pair_value.append(value)
    elif state == 1:
        state = 2
        moves += 1
        l.set_text("Moves="+str(moves))
        pair_position.append(position)
        pair_value.append(value)
    else:
        state = 1 
        if (pair_value[0] != pair_value[1]):
            exposed[pair_position[0]] = False
            exposed[pair_position[1]] = False
        pair_position = []
        pair_value = [] 
        pair_position.append(position)
        pair_value.append(value)
                    
     
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global card_number, exposed
    for i in range(16):
        if exposed[i] == False:
            canvas.draw_polygon([(0+i*50, 0), (50+i*50, 0),(50+i*50,100),(0+i*50, 100)], 1, "White", "Green")
        else:
            canvas.draw_text(str(card_number[i]), (25+i*50,50), 24, "White")

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
l=frame.add_label("Moves = 0")



# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()


# Always remember to review the grading rubric
