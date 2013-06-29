# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console


# initialize global variables used in your code
secret_number=0
count=0
min=0
max=0

# define event handlers for control panel
import random
import simplegui
import math

def init(low,high):
    global count
    global secret_number
    global min
    global max
    min=low
    max=high
    count = math.ceil(math.log((high-low+1),2))
    secret_number= random.randrange(low,high)
    print "________________________________________"
    print "New game. Range is from", low, "to", high
    print "Number of remaining guesses is", count
    print "the secret number was",secret_number
    


    
    
def range100():
    global min
    global max
    min=0
    max=100
    # button that changes range to range [0,100) and restarts
    init(0,100)
    return secret_number
   
  
    

def range1000():
    # button that changes range to range [0,1000) and restarts
    init(0,1000)
    global min
    global max
    min=0
    max=1000
    return secret_number

def get_input(guess):
    # main game logic goes here	
    global count
    global secret_number
    global min
    global max
    count-=1
    if count < 0:
        result = "you lose this game"
        print result
        print "The secret number is" , secret_number
        init(min,max)
    elif int(guess)==secret_number:
        print "guess was",guess
        print "correct"
        print "number of remining guess is", count
        init(min,max)
    else:
        if int(guess) > secret_number:
            result = "higher"
        elif int(guess) < secret_number:
            result = "lower"
        print "Guess was", guess
        print "number of remining guess is ", count
        print result
    
        
    
    
   
    
    
   
    
# create frame
f= simplegui.create_frame("guess the number", 200, 200)

# register event handlers for control elements
f.add_button("Range is [0,100)", range100,200)
f.add_button("Range is [0,1000)", range1000,200)
f.add_input("Enter a guess", get_input,200)

init(0,100)
# start frame
f.start()

# always remember to check your completed program against the grading rubric
