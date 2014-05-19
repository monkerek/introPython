# http://www.codeskulptor.org/#user31_R0dpyjesB4_7.py
# =============



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
        self.lis = []

    def __str__(self):
        res = "Hand contains"
        for card in self.lis:
            res += (' ' + card.__str__())
        return res

    def add_card(self, card):
        self.lis.append(card)

    def get_value(self):
        value = 0
        ace_count = 0
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        for card in self.lis:
            rank = card.get_rank()
            value += VALUES[rank]
            if rank == 'A':
                ace_count += 1
        
        if ace_count >= 1 and value + 10 <= 21:
            value += 10
        
        return value
    
    def draw(self, canvas, pos):
        for index in range(len(self.lis)):
            if index == 5:
                break
            self.lis[index].draw(canvas, [pos[0] + index * (CARD_SIZE[0] + 10), pos[1]])
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.lis = []
        for suit in SUITS:
            for rank in RANKS:
                self.lis.append(Card(suit, rank))

    def shuffle(self):
        # shuffle the deck 
        # use random.shuffle()
        random.shuffle(self.lis)

    def deal_card(self):
        card = self.lis[-1]
        self.lis.pop()
        return card
        
    def __str__(self):
        # return a string representing the deck
        res = "Deck contains"
        for card in self.lis:
            res += (' ' + card.__str__())
        return res



#define event handlers for buttons
def deal():
    global outcome, in_play, score
    
    if in_play:
        outcome = 'The dealer wins'
        in_play = False
        score -= 1
        return
    
    global deck
    deck = Deck()
    deck.shuffle()
    
    global player, dealer
    
    player = Hand()
    player.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    
    dealer = Hand()
    dealer.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    
    #print "Player" + player.__str__()
    #print "Dealer" + dealer.__str__()
    
    in_play = True
    outcome = ""
    
def hit():
    global outcome, in_play, score, player, deck
    
    if not in_play:
        return
    
    if player.get_value() <= 21:
        player.add_card(deck.deal_card())
        if player.get_value() > 21:
            outcome = 'You have busted'
            #print outcome
            in_play = False
            score -= 1
    
 
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global outcome, in_play, dealer, player, deck, score
    if not in_play:
        return
    else:
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
        
        if dealer.get_value() > 21:
            outcome = "The dealer has busted"
            #print outcome
            in_play = False
            score += 1
        else:
            if player.get_value() <= dealer.get_value():
                outcome = "The dealer wins"
                #print outcome
                in_play = False
                score -= 1
            else:
                outcome = "You win"
                #print outcome
                in_play = False
                score += 1
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    global score, player, dealer, in_play, outcome
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text('Blackjack', (80, 80), 50, 'White')
    canvas.draw_text('Score: ', (400,80), 30, 'White')
    canvas.draw_text(str(score), (540,80), 30, 'White')
    canvas.draw_text('Dealer', (80,165), 30, 'White')
    canvas.draw_text('Player', (80,365), 30, 'White')
    
    canvas.draw_text(str(outcome), (300,165), 30, 'White')

    player.draw(canvas, [80,400])
    dealer.draw(canvas, [80,200])
    
    if in_play:
        canvas.draw_text('Hit or stand?', (350,365), 30, 'White')
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [116,250], CARD_SIZE)
    else:
        canvas.draw_text('New deal?', (350,365), 30, 'White')


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()
