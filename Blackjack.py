#lets go Gambling!
import tkinter as tk
from PIL import Image, ImageTk
import pygame
import random


global card2

#5-Card Charlie In the world of blackjack,
#the 5-Card Charlie rule is applied when a player hits five cards but their hand's total value is still less than 21,
#they will receive an automatic win.


#card rules one of spade diamond hearts club each
#4 aces
#4 kings
#4 queens
#4 jacks
#4 tens
#4 nines
#4 eights
#4 sevens
#4 sixes
#4 fives
#4 fours
#4 threes
#4 twos


#main casino window
casino = tk.Tk()
#title of the window
casino.title("Casino Floor")
#sets size of window
casino.geometry("1000x1000")



card1 = [
     "1 Ace of Spades",
     "1 Ace of Hearts",
     "1 Ace of Diamonds",
     "1 Ace of Clubs",
     "2 of Spades",
     "2 of Hearts",
     "2 of Diamonds",
     "2 of Clubs",
     "3 of Spades",
     "3 of Hearts",
     "3 of Diamonds",
     "3 of Clubs",
     "4 of Spades",
     "4 of Hearts",
     "4 of Diamonds",
     "4 of Clubs",
     "5 of Spades",
     "5 of Hearts",
     "5 of Diamonds",
     "5 of Clubs",
     "6 of Spades",
     "6 of Hearts",
     "6 of Diamonds",
     "6 of Clubs",
     "7 of Spades",
     "7 of Hearts",
     "7 of Diamonds",
     "7 of Clubs",
     "8 of Spades",
     "8 of Hearts",
     "8 of Diamonds",
     "8 of Clubs",
     "9 of Spades",
     "9 of Hearts",
     "9 of Diamonds",
     "9 of Clubs",
     "10 of Spades",
     "10 of Hearts",
     "10 of Diamonds",
     "10 of Clubs",
     "10 Jack of Spades",
     "10 Jack of Hearts",
     "10 Jack of Diamonds",
     "10 Jack of Clubs",
     "10 Queen of Spades",
     "10 Queen of Hearts",
     "10 Queen of Diamonds",
     "10 Queen of Clubs",
     "10 King of Spades",
     "10 King of Hearts",
     "10 King of Diamonds",
     "10 King of Clubs"
    ]

card_value = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10}


           
                                   

card2 = [None] * 52

#move just one card
#move_card is the function
#card1 orignial deck all cards there
#card2 cards moving to empty at the start
#mov_card(card1, card2, 1)

#0-51
#card_to_deck():

# aces
# kings
# queens
# jacks
# tens
# nines
# eights
# sevens
# sixes
# fives
# fours
# threes
# twos

#purpose
#Random_sort():
    
    


#random sort
#52 carts in a deck
#generate random number 1-52 put new card there if card there random number
# 1-52 until card isn't in index spot

#blackjack shuffle deck use random sort
#pulls for top card realistically like real deck


#the loop will end when all cards move to the card2
#the loop will break due to the nature of while true and break ending loop

#fisher-yates
#also known as knuth shuffle
#an algorithm for shuffling a finite sequence
#iterates through list from last element to the second element
#for each element, swapping it with a randomly selected element from the
#remaining unshuffled portion of the list

#idea 1 pretty slow
"""
def fisher_yates(card2, card1):
    for i in range(len(card2) - 1,  0, -1):
        j = random.randint(0, i)
        card2[i], card2[j] = card2[j], card2[i]     
  #  for i in range(len(card2)):
       # card2[i] = card2[i]
    return card2
 """       
        
#idea 2 found out .shuffle already exists on google
#enumerate allows to iterate through a sequence and keep track of index of each element
def fisher_yates():
    for i in range(len(card2)):
        card2[i] = None
    shuffled_deck = card1[:]#creates a copy of card1
    random.shuffle(shuffled_deck)
    for i, card in enumerate(shuffled_deck):
        card2[i] = card
        print("cards being placed")
    print(card2)
    randomgendeck_button.config(state='disable')
    fishergendeck_button.config(state='disable')
    End_button.config(state='normal')
    start_button.config(state='normal')







#python enumerate allows you to iterate through a sequence
#and keep track of the index of each element


#random_sort takes 'card' then gens random number moves to empty spot in second 'deck'
#if spot is taken then generates a random number again until an empty spot is found.
def Random_sort(card1, card2):
    global randomgendeck
    for i in range(len(card2)):
        card2[i] = None
    #loops through the base deck and shuffle the cards the shuffled deck
    for key, value in enumerate(card1):
        #A while loop runs while a condition is true - reddit
        while True:
            random_key1 = random.randint(0,51)
            if card2[random_key1] is None:
                card2[random_key1] = value
                #f starts text with data
                #'{}' to include a value in text
                print(f"Moved card '{value}' to spot {random_key1} in shuffled deck.")
                #ends the loop when the condition has been meet.
                break
            else:
                print(f"Spot {random_key1} is not empty, reshuffling.")
    print(card2)
    randomgendeck_button.config(state='disable')
    fishergendeck_button.config(state='disable')
    End_button.config(state='normal')
    start_button.config(state='normal')

#index of shuffled deck
global cardindex
global playtextfin, playtext1, playtext2, playtext3, playtext4, playtext5,player_score

cardindex = 0
global cardhitme, cardmaxplay
cardhitme = 0
cardmaxplay = 0
player_score = 0
#player number
player_score = 0
playtext1 = ""
playtext2 = ""
playtext3 = ""
playtext4 = ""
playtext5 = ""
playtextfin = ""


#main function: controls the logic for player hitting
def hitme():
    global cardindex, cardhitme, cardmaxplay, card_value, player_score

    if cardindex >= len(card2) or cardhitme >= 4:
        return

    new_card = card2[cardindex]
    cardindex += 1
    cardmaxplay += 1

    #Correctly update the value from the current card
    value = new_card.split()[0]
    player_score += card_value.get(value, 0)
    playernum_score.config(text=f"Score: {player_score}")

    if cardhitme == 0:
        current_text = playernum_2.cget("text")
        updated_text = current_text + " " + new_card if current_text else new_card
        playernum_2.config(text=updated_text)

    elif cardhitme == 1:
        current_text = playernum_3.cget("text")
        updated_text = current_text + " " + new_card if current_text else new_card
        playernum_3.config(text=updated_text)

    elif cardhitme == 2:
        current_text = playernum_4.cget("text")
        updated_text = current_text + " " + new_card if current_text else new_card
        playernum_4.config(text=updated_text)

    elif cardhitme == 3:
        current_text = playernum_5.cget("text")
        updated_text = current_text + " " + new_card if current_text else new_card
        playernum_5.config(text=updated_text)

    cardhitme += 1

    if cardhitme >= 4 or cardindex >= len(card2):
        hitme_button.config(state='disable')
        #handles logic for player score 
    if  player_score >= 21:
        hitme_button.config(state='disabled')
        print("OVER 21 YOU BUSTED")
    if cardhitme >= 4 and player_score >= 21:
       print("CHARLIES RULE PLAYER WINS")
    
    




#first go at a hit me fuction
#    text = playernum_1.cget("text")
#    pnum1 = int(text[:2].strip())
#    cardindex += 1
#    text2 = playernum_2.cget("text")
#    cardindex = int(text2[:2].strip())
#    playernum_2.config(text=f"{pnum2}")
    
    
    
#stand function    
def stand():
    global cardindex, cardhitmedeal, cardmaxplaydeal, dealer_score
    dealer_score = 0
    cardhitmedeal = 0

    # Disable player's "Hit Me" button once they stand
    hitme_button.config(state='disabled')

    # Dealer hits while score < 17, and has fewer than 5 cards, and cards left in deck
    while dealer_score < 17 and cardhitmedeal < 5 and cardindex < len(card2):
        new_card = card2[cardindex]
        cardindex += 1
        cardhitmedeal += 1
        #take rank and add it to dealer score
        rank = new_card.split()[0]
        dealer_score += card_value.get(rank, 0)
        #dealer card display labels
        if cardhitmedeal == 1:
            current_text = dealernum_1.cget("text")
            dealernum_1.config(text=f"{new_card}".strip())
        elif cardhitmedeal == 2:
            current_text = dealernum_2.cget("text")
            dealernum_2.config(text=f"{new_card}".strip())
        elif cardhitmedeal == 3:
            current_text = dealernum_3.cget("text")
            dealernum_3.config(text=f"{new_card}".strip())
        elif cardhitmedeal == 4:
            current_text = dealernum_4.cget("text")
            dealernum_4.config(text=f"{new_card}".strip())
        elif cardhitmedeal == 5:
            current_text = dealernum_5.cget("text")
            dealernum_5.config(text=f"{new_card}".strip())

    #Show dealer's final score
    dealernumfin.config(text=f"Score: {dealer_score}")
    stand_button.config(state='disabled')
    #winner & loser logic
    if dealer_score > 21:
        print("DEALER BUSTS, PLAYER WINS")
    elif player_score > 21:
        print("PLAYER BUSTS, DEALER WINS")
    elif dealer_score > player_score:
        print("DEALER WINS")
    elif dealer_score < player_score:
        print("PLAYER WINS")
    else:
       print("IT'S A TIE")


    

#resets the casino floor
def resetalg():
    global card2
    card2 = [None] * 52
    randomgendeck_button.config(state='normal')
    fishergendeck_button.config(state='normal')
    playernum_1.config(text="")
    playernum_2.config(text="")
    playernum_3.config(text="")
    playernum_4.config(text="")
    playernum_5.config(text="")
    playernum_score.config(text="")
    dealernum_1.config(text="")
    dealernum_2.config(text="")
    dealernum_3.config(text="")
    dealernum_4.config(text="")
    dealernum_5.config(text="")
    dealernumfin.config(text="")
        

#starts the game gets everything ready
def startgame():
    global cardindex, cardhitme, player_score, card_value
    cardindex = 0
    cardhitme = 0
    #new score for new game!
    player_score = 0 
    hitme_button.config(state='normal')
    stand_button.config(state='normal')
    #dealer first card
    dealernum_1.config(text=card2[cardindex])
    cardindex += 1
    #player first card
    player_card = card2[cardindex]
    playernum_1.config(text=player_card)
    cardindex += 1

    #value and update score
    value = player_card.split()[0]
    player_score += card_value.get(value, 0)
    playernum_score.config(text=f"Score: {player_score}")

#resets buttons when player is done 
def END_GAME_FUNC():
    hitme_button.config(state='disable')
    stand_button.config(state='disable')
    randomgendeck_button.config(state='normal')
    fishergendeck_button.config(state='normal')
     


    
                  
#random_sort - very slow sometimes works before python gives up 
#fisher_yates algorithms is exactly what the doctor ordered!

#generates the deck(see rules above)
#lambda to mean the command doesn't run when the program starts, a delay of sorts.
#random_sort deck shuffle
#alg buttons
randomgendeck_button = tk.Button(casino, text="Random_sort Shuffle",
font=("Arial", 20), fg="white", bg="Black",command=lambda: Random_sort(card1, card2))
randomgendeck_button.place(x=50, y=50)

#fisher_yates deck shuffle algorithms
fishergendeck_button = tk.Button(casino, text="Fisher-yates Shuffle",
font=("Arial", 20), fg="white", bg="Black",command=lambda: fisher_yates())
fishergendeck_button.place(x=50, y=120)

#reset algorithms
resetalg_button = tk.Button(casino, text="Reset Deck",
font=("Arial", 20), fg="white", bg="Black",command=lambda: resetalg())
resetalg_button.place(x=50, y=220)


#x is left and right
#y is up and down


#game buttons
#hit me!
hitme_button = tk.Button(casino, text="Hit Me",
font=("Arial", 20), fg="white", bg="Black",command=lambda: hitme())
hitme_button.place(x=800, y=420)

#Stand
stand_button = tk.Button(casino, text="Stand",
font=("Arial", 20), fg="white", bg="Black",command=lambda: stand())
stand_button.place(x=800, y=520)

#Start game - activates game buttons disables alg buttons
start_button = tk.Button(casino, text="Start Game",
font=("Arial", 20), fg="white", bg="Black",command=lambda: startgame())
start_button.place(x=800, y=320)

#End game - disables game buttons activates alg buttons
End_button = tk.Button(casino, text="End Game",
font=("Arial", 20), fg="white", bg="Black",command=lambda: END_GAME_FUNC())
End_button.place(x=800, y=220)


#player labels
#dealer labels

#1dealer
dealernum_1 = tk.Label(casino, text= "", font=("Arial", 24), fg="white", bg = "red")
dealernum_1.place(x=400,y=50)

#2dealer
dealernum_2 = tk.Label(casino, text= "", font=("Arial", 24), fg="white", bg = "red")
dealernum_2.place(x=400,y=100)

#3dealer
dealernum_3 = tk.Label(casino, text= "", font=("Arial", 24), fg="white", bg = "red")
dealernum_3.place(x=400,y=150)

#4dealer
dealernum_4 = tk.Label(casino, text= "", font=("Arial", 24), fg="white", bg = "red")
dealernum_4.place(x=400,y=200)

#5dealer
dealernum_5 = tk.Label(casino, text= "", font=("Arial", 24), fg="white", bg = "red")
dealernum_5.place(x=400,y=250)

#score dealer
dealernumfin = tk.Label(casino, text= "DEAL", font=("Arial", 24), fg="white", bg = "red")
dealernumfin.place(x=400,y=300)




#player numbers

#1player
playernum_1 = tk.Label(casino, text= "", font=("Arial", 24), fg="white", bg = "grey")
playernum_1.place(x=450,y=350)

#2player
playernum_2 = tk.Label(casino, text= "", font=("Arial", 24), fg="white", bg = "grey")
playernum_2.place(x=450,y=400)

#3player
playernum_3 = tk.Label(casino, text= "", font=("Arial", 24), fg="white", bg = "grey")
playernum_3.place(x=450,y=450)

#4player
playernum_4 = tk.Label(casino, text= "", font=("Arial", 24), fg="white", bg = "grey")
playernum_4.place(x=450,y=500)

#5player
playernum_5= tk.Label(casino, text= "", font=("Arial", 24), fg="white", bg = "grey")
playernum_5.place(x=450,y=550)

#score player
playernum_score = tk.Label(casino, text= "DEAL", font=("Arial", 24), fg="white", bg = "grey")
playernum_score.place(x=450,y=600)




#name labels
playername = tk.Label(casino, text= "YOU", font=("Arial", 24), fg="white", bg = "Gray")
playername.place(x=350,y=500)

dealername = tk.Label(casino, text= "DEALER", font=("Arial", 24), fg="white", bg = "Red")
dealername.place(x=720,y=100)



#disables buttons on start up
hitme_button.config(state='disable')
End_button.config(state='disable')
start_button.config(state='disable')
stand_button.config(state='disable')


#runs the application(keep at the bottom)
casino.mainloop()
