# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
ball_pos = [WIDTH/2,HEIGHT/2]
ball_vel = [0,0]
score1 = 0
score2 = 0
paddle1_pos = HEIGHT/2
paddle2_pos = HEIGHT/2
paddle1_vel = 0
paddle2_vel = 0
right = 'true'

# helper function that spawns a ball, returns a position vector and a velocity vector
# if right is True, spawn to the right, else spawn to the left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2,HEIGHT/2]
    ball_vel = [8,4]
    if right:
        balldir = 1
    else:
        balldir = -1
    ball_vel[0]= random.randrange(120,140)/100*balldir
    ball_vel[1]= random.randrange(60,180)/100*balldir
    ball_pos[0]+=ball_vel[0]
    ball_pos[1]+=ball_vel[1]

# define event handlers
def init():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    ball_init(right)
    score1 = 0
    score2 = 0
    pass

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global paddle1_vel, paddle2_vel
 
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos = paddle1_pos+paddle1_vel
    if paddle1_pos <= HALF_PAD_HEIGHT or paddle1_pos >= HEIGHT-HALF_PAD_HEIGHT:
        paddle1_vel = -paddle1_vel
    paddle2_pos = paddle2_pos+paddle2_vel
    if paddle2_pos <= HALF_PAD_HEIGHT or paddle2_pos >= HEIGHT-HALF_PAD_HEIGHT:
        paddle2_vel = -paddle2_vel
    
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    c.draw_polygon([(PAD_WIDTH, paddle1_pos-HALF_PAD_HEIGHT),(0, paddle1_pos-HALF_PAD_HEIGHT), (0, paddle1_pos+HALF_PAD_HEIGHT), (PAD_WIDTH,paddle1_pos+HALF_PAD_HEIGHT)], 1, "white","White")
    c.draw_polygon([ (WIDTH-PAD_WIDTH, paddle2_pos-HALF_PAD_HEIGHT),(WIDTH, paddle2_pos-HALF_PAD_HEIGHT),(WIDTH, paddle2_pos+HALF_PAD_HEIGHT), (WIDTH-PAD_WIDTH,paddle2_pos+HALF_PAD_HEIGHT)], 1, "White","White")
     
    # update ball
    
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= (HEIGHT-1)-BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    elif ball_pos[0] <= BALL_RADIUS+PAD_WIDTH: 
        ball_vel[0] = -ball_vel[0]
        if ball_pos[1]<= paddle1_pos-HALF_PAD_HEIGHT or ball_pos[1] >= paddle1_pos+HALF_PAD_HEIGHT:
            score2 +=1
            ball_pos = [WIDTH/2,HEIGHT/2]
        else:
            ball_vel[0]=ball_vel[0]*1.1
    elif ball_pos[0] >= (WIDTH-1)-(BALL_RADIUS+PAD_WIDTH):
        ball_vel[0] = -ball_vel[0]
        if ball_pos[1]<= paddle2_pos-HALF_PAD_HEIGHT or ball_pos[1] >= paddle2_pos+HALF_PAD_HEIGHT:
            score1 +=1
            ball_pos = [WIDTH/2,HEIGHT/2]
        else:
            ball_vel[0]=ball_vel[0]*1.1
        
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
                           
 
            
    # draw ball and scores
    c.draw_circle([ball_pos[0], ball_pos[1]],BALL_RADIUS , 12, "White","white")
    c.draw_text(str(score1), [200,100], 28, "White")
    c.draw_text(str(score2), [400,100], 28, "White")    
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    acc = 5
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel -= acc
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel += acc
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel += acc
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel -= acc
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", init, 100)


# start frame
init()
frame.start()

