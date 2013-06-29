# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
message = "Game Begin!"
message2=""
sum_player = 0
sum_dealer = 0
dealer = None
player = None
my_deck = None
player_state = None

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class	
class Hand:
    
    def __init__(self):
         self.cards = []
            
    def __str__(self):
        buff = []
        for i in self.cards:
            buff.append(str(i))
        return str(buff)
        
    def add_card(self, card):
        self.cards.append(card)
        
    # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
    def get_value(self):
        global VALUES
        self.sum_cards = 0
        sign = False
        for i in self.cards:
            self.sum_cards += VALUES[i.get_rank()]
            if i.get_rank()=='A':
                sign = True
        if sign == True and self.sum_cards +10 <22:
            return self.sum_cards+10
        else: 
            return self.sum_cards
    
    
 
    def busted(self):
        if self.get_value()>21:
            return True
        else:
            return False
    
    def draw(self, canvas, p):
        for c in self.cards:
            c.draw(canvas,[p[0]+self.cards.index(c)*CARD_SIZE[0],p[1]])

# define deck class
class Deck:
    def __init__(self):
        global SUITS, RANKS
        self.cards = []
        for s in SUITS:
            for r in RANKS:
                self.cards.append(Card(s,r))

    # add cards back to deck and shuffle
    def shuffle(self):
        random.shuffle(self.cards)
       

    def deal_card(self):
            card = self.cards.pop()
            return card
       
    def __str__(self):
        buff = []
        for i in self.cards:
            buff.append(str(i))
        return str(buff)


#define event handlers for buttons
def deal():
    global outcome,in_play,score,message,sum_dealer,sum_player,dealer, player,message2,player_state
    global my_deck
    message = ""
    message2 = "Stand or Hit?"
    my_deck = Deck()
    my_deck.shuffle()
    dealer = Hand()
    player = Hand()
    for d in range(2):        
        dealer.add_card(my_deck.deal_card())
        player.add_card(my_deck.deal_card())
    sum_dealer = dealer.get_value()
    sum_player = player.get_value()
    in_play = True
    player_state = True

def hit():
    global in_play, score, message,sum_player,player,dealer,my_deck,message2
    
    # replace with your code below
    # if the hand is in play, hit the player
    if in_play == False:
        return
    else:
        player.add_card(my_deck.deal_card())
        sum_player = player.get_value()
        if sum_player > 21:
            in_play = False
            score -= 1
            player_state = False
            message = "You busted! You lose"
            message2 = "New deal?"
        else:
            in_play = True
            message = ""
            message2 = "Stand or Hit?"
            return player.get_value()    
    
    # if busted, assign an message to outcome, update in_play and score
    
         
        
def stand():
    
        # replace with your code below
    global in_play, score, sum_player,sum_dealer,dealer,player,message2,message,player_state
    player_state = False
    if in_play == True:
        while dealer.get_value() <=17:            
            dealer.add_card(my_deck.deal_card())
            sum_dealer = dealer.get_value()
        if dealer.get_value() > 21:
            in_play = False
            score += 1
            message = "Dealer busted,You Win!"
            message2 = "New deal?"
        else:
            in_play = False
            if sum_player > sum_dealer:
                score += 1
                message = "You Win!"
                message2 = "New deal?"
            else:
                score -= 1
                message = "You lose!"
                message2= "New deal?"
    else:
        return
            
            
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score
def init():
    global score,message,messange2
    score = 0
    deal()
    message = "Game Begin!"
    
  

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global message,score,dealer,player,my_deck,message2,in_play
    if player_state == False:
        dealer.draw(canvas,[100,180])
        player.draw(canvas, [100, 380])
    elif player_state == True:
        player.draw(canvas, [100, 380])
        dealer.draw(canvas,[100,180])
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [100+CARD_CENTER[0],180+CARD_CENTER[1]],CARD_BACK_SIZE)
    canvas.draw_text("Blackjack", [100,100], 36, 'Blue')
    canvas.draw_text("Score ="+ str(score), [350,100], 20, 'white')
    canvas.draw_text("Dealer", [100,150], 20, 'white')
    canvas.draw_text("Player", [100,330], 20, 'white')
    canvas.draw_text(message, [300,150], 20, 'white')
    canvas.draw_text(message2, [300,330], 20, 'white')


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
my_deck = Deck()
dealer = Hand()
player = Hand()
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# deal an initial hand
init()



# get things rolling
frame.start()


# remember to review the gradic rubric
