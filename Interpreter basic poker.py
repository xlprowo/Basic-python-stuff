#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random
print ("Welcome to the poker python game, are you ready to play?")
start_the_game = input("Type something when you're ready ")

if start_the_game == "yes":
    card_1 = random.randint(1,12)
    card_2 = random.randint(1,12)
    card_3 = random.randint(1,12)
print(f"This are your first three cards: {card_1}, {card_2}, {card_3}")

initial_bet = (input("Place your bet "))

dealer_card_1=random.randint(1,12)
dealer_card_2=random.randint(1,12)
dealer_card_3=random.randint(1,12)

print(f"These are the dealer's cards: {dealer_card_1}, {dealer_card_2}, {dealer_card_3}")

card_4 = random.randint(1,12)
print(f"This is your fourth card: {card_4}")
want_a_second_bet = input("Do you want to place a second bet? ")
if want_a_second_bet == "yes":
    second_bet = input("How much do you want to bet? ")
else:
    second_bet = 0
card_5 = random.randint(1,12)
print(f"this is your last card: {card_5}")
print(f"your cards are: {card_1}, {card_2}, {card_3}, {card_4}, {card_5}")

want_a_last_bet =input("Do you want to place a last bet? ")
if want_a_last_bet == "yes":
    last_bet= input("How much are you willing to bet? ")
else:
    last_bet = 0

try:
    
    initial_bet = float(initial_bet)
    second_bet = float(second_bet)
    last_bet = float(last_bet)
    final_bet = initial_bet + second_bet + last_bet
    
except:
    
    print("You did not insert a valid number, bet cancelled")
    final_bet = 0
   

dealer_card_4 = random.randint(1,12)
dealer_card_5 = random.randint(1,12)
print(f"here are the dealers cards: \n {dealer_card_1}, {dealer_card_2}, {dealer_card_3}, {dealer_card_4}, {dealer_card_5}")

players_game =[card_1, card_2, card_3, card_4, card_5]
dealers_game =[dealer_card_1, dealer_card_2, dealer_card_3, dealer_card_4, dealer_card_5]

user_final_game = "nogame"
dealer_final_game = "nogame"
count_card_1 = players_game.count(card_1)
count_card_2 = players_game.count(card_2)
count_card_3 = players_game.count(card_3)
count_card_4 = players_game.count(card_4)
count_card_5 = players_game.count(card_5)

while count_card_1 + count_card_2 + count_card_3 + count_card_4 + count_card_5 == 9:
    if (count_card_1 == 2 and count_card_2 == 2 ) or(count_card_1 == 2 and count_card_3 == 2) or (count_card_1 == 2 and count_card_4 == 2)  or (count_card_1 == 2 and count_card_5 == 2):
        user_final_game = "twopairs"
        break
    elif (count_card_2 == 2 and count_card_1 == 2 ) or(count_card_2 == 2 and count_card_3 == 2) or (count_card_2 == 2 and count_card_4 == 2)  or (count_card_2 == 2 and count_card_5 == 2):
        user_final_game = "twopairs"
        break
    elif (count_card_3 == 2 and count_card_1 == 2 ) or(count_card_3 == 2 and count_card_2 == 2) or (count_card_3 == 2 and count_card_4 == 2)  or (count_card_3 == 2 and count_card_5 == 2):
        user_final_game = "twopairs"
        break
    elif (count_card_4 == 2 and count_card_1 == 2 ) or(count_card_4 == 2 and count_card_2 == 2) or (count_card_4 == 2 and count_card_3 == 2)  or (count_card_4 == 2 and count_card_5 == 2):
        user_final_game = "twopairs"
        break
    elif (count_card_5 == 2 and count_card_1 == 2 ) or(count_card_5 == 2 and count_card_2 == 2) or (count_card_5 == 2 and count_card_3 == 2)  or (count_card_5 == 2 and count_card_4 == 2):
        user_final_game = "twopairs"
        break

while count_card_1 + count_card_2 + count_card_3 + count_card_4 + count_card_5 == 7:
    if count_card_1 == 2:
        user_final_game = "pair"
        break
    elif count_card_2 == 2: 
        user_final_game = "pair"
        break
    elif count_card_3 == 2:
        user_final_game = "pair"
        break
    elif count_card_4 == 2:
        user_final_game = "pair"
        break
    elif count_card_5 == 2:
        user_final_game = "pair"
        break

if count_card_1 + count_card_2 + count_card_3 + count_card_4 + count_card_5 == 13:
    user_final_game = "fullhouse"
    
if count_card_1 == 3 :
    user_final_game = "threeofakind"
elif count_card_2 == 3: 
    user_final_game = "threeofakind"
elif count_card_3 == 3:
    user_final_game = "threeofakind"
elif count_card_4 == 3:
    user_final_game = "threeofakind"
elif count_card_5 == 3:
    user_final_game = "threeofakind"

if count_card_1 == 4 :
    user_final_game = "fourofakind"
elif count_card_2 == 4: 
    user_final_game = "fourofakind"
elif count_card_3 == 4:
    user_final_game = "fourofakind"
elif count_card_4 == 4:
    user_final_game = "fourofakind"
elif count_card_5 == 4:
    user_final_game = "fourofakind"

if count_card_1 == 5:
    user_final_game = "fiveofakind"
elif count_card_2 == 5: 
    user_final_game = "fiveofakind"
elif count_card_3 == 5:
    user_final_game = "fiveofakind"
elif count_card_4 == 5:
    user_final_game = "fiveofakind"
elif count_card_5 == 5:
    user_final_game = "fiveofakind"


#dealers proces to define kind of play 

dealercount_card_1 = dealers_game.count(dealer_card_1)
dealercount_card_2 = dealers_game.count(dealer_card_2)
dealercount_card_3 = dealers_game.count(dealer_card_3)
dealercount_card_4 = dealers_game.count(dealer_card_4)
dealercount_card_5 = dealers_game.count(dealer_card_5)


while dealercount_card_1 + dealercount_card_2 + dealercount_card_3 + dealercount_card_4 + dealercount_card_5 == 9:
    if (dealercount_card_1 == 2 and dealercount_card_2 == 2 ) or(dealercount_card_1 == 2 and dealercount_card_3 == 2) or (dealercount_card_1 == 2 and dealercount_card_4 == 2)  or (dealercount_card_1 == 2 and dealercount_card_5 == 2):
        dealer_final_game = "twopairs"
        break
    elif (dealercount_card_2 == 2 and dealercount_card_1 == 2 ) or(dealercount_card_2 == 2 and dealercount_card_3 == 2) or (dealercount_card_2 == 2 and dealercount_card_4 == 2)  or (dealercount_card_2 == 2 and dealercount_card_5 == 2):
        dealer_final_game = "twopairs"
        break
    elif (dealercount_card_3 == 2 and dealercount_card_1 == 2 ) or(dealercount_card_3 == 2 and dealercount_card_2 == 2) or (dealercount_card_3 == 2 and dealercount_card_4 == 2)  or (dealercount_card_3 == 2 and dealercount_card_5 == 2):
        dealer_final_game = "twopairs"
        break
    elif (dealercount_card_4 == 2 and dealercount_card_1 == 2 ) or(dealercount_card_4 == 2 and dealercount_card_2 == 2) or (dealercount_card_4 == 2 and dealercount_card_3 == 2)  or (dealercount_card_4 == 2 and dealercount_card_5 == 2):
        dealer_final_game = "twopairs"
        break
    elif (dealercount_card_5 == 2 and dealercount_card_1 == 2 ) or(dealercount_card_5 == 2 and dealercount_card_2 == 2) or (dealercount_card_5 == 2 and dealercount_card_3 == 2)  or (dealercount_card_5 == 2 and dealercount_card_4 == 2):
        dealer_final_game = "twopairs"
        break

while dealercount_card_1 + dealercount_card_2 + dealercount_card_3 + dealercount_card_4 + dealercount_card_5 == 7:
    if dealercount_card_1 == 2 :
        dealer_final_game = "dealerpair"
        break
    elif dealercount_card_2 == 2: 
        dealer_final_game = "dealerpair"
        break
    elif dealercount_card_3 == 2:
        dealer_final_game = "dealerpair"
        break
    elif dealercount_card_4 == 2:
        dealer_final_game = "dealerpair"
        break
    elif dealercount_card_5 == 2:
        dealer_final_game = "dealerpair"
        break

if dealercount_card_1 + dealercount_card_2 + dealercount_card_3 + dealercount_card_4 + dealercount_card_5 == 13:
    dealer_final_game = "dealerfullhouse"    

if dealercount_card_1 == 3 :
    dealer_final_game = "dealerthreeofakind"
elif dealercount_card_2 == 3: 
    dealer_final_game = "dealerthreeofakind"
elif dealercount_card_3 == 3:
    dealer_final_game = "dealerthreeofakind"
elif dealercount_card_4 == 3:
    dealer_final_game = "dealerthreeofakind"
elif dealercount_card_5 == 3:
    dealer_final_game = "dealerthreeofakind"


if dealercount_card_1 == 4 :
    dealer_final_game = "dealerfourofakind"
elif dealercount_card_2 == 4: 
    dealer_final_game = "dealerfourofakind"
elif dealercount_card_3 == 4:
    dealer_final_game = "dealerfourofakind"
elif dealercount_card_4 == 4:
    dealer_final_game = "dealerfourofakind"
elif dealercount_card_5 == 4:
    dealer_final_game = "dealerfourofakind"


if dealercount_card_1 == 5:
    dealer_final_game = "dealerfiveofakind"
elif dealercount_card_2 == 5: 
    dealer_final_game = "dealerfiveofakind"
elif dealercount_card_3 == 5:
    dealer_final_game = "dealerfiveofakind"
elif dealercount_card_4 == 5:
    dealer_final_game = "dealerfiveofakind"
elif dealercount_card_5 == 5:
    dealer_final_game = "dealerfiveofakind"

if user_final_game == "fiveofakind" and dealer_final_game == "dealerfiveofakind":
    user_final_game = "draw"
    dealer_final_game = "draw"
    print("This is impossible! The dealer and you have five of a kind! You're both winners")
elif user_final_game == "fiveofakind":
    user_final_game = "winner"
    print("You win! Five of a kind! You're really lucky")
elif dealer_final_game == "dealerfiveofakind":
    dealer_final_game = "winner"
    print("The dealer is one lucky bastard! Five of a kind! You lose!")
elif user_final_game == "fourofakind" and dealer_final_game == "dealerfourofakind":
    user_final_game = "draw"
    dealer_final_game = "draw"
    print ("Four of a kind for you and the dealer! It's a tie. What a game!")
elif user_final_game =="fourofakind":
    user_final_game = "winner"
    print("You have four of a kind!")
    print("You win!")
elif dealer_final_game == "dealerfourofakind":
    dealer_final_game = "winner"
    print("You lose, the dealer has four of a kind!")
elif user_final_game == "fullhouse" and dealer_final_game == "dealerfullhouse":
    user_final_game = "draw"
    dealer_final_game = "draw"
    print("You and the dealer have a Fullhouse! Nice game!")
elif user_final_game == "fullhouse":
    user_final_game = "winner"
    print("Full house, you win!")
elif dealer_final_game == "dealerfullhouse" :
    dealer_final_game ="winner"
    print("Full house, the dealer wins")
elif user_final_game == "threeofakind" and dealer_final_game == "dealerthreeofakind":
    user_final_game = "draw"
    dealer_final_game = "draw"
    print ("It's a tie both, the dealer and you have three of a kind")
elif user_final_game == "threeofakind":
    user_final_game = "winner"
    print("You win because you have threeofakind!")
elif dealer_final_game =="threeofakind":
    dealer_final_game = "winner"
    print("Dealer wins, he has three of a kind")
elif user_final_game == "twopairs" and dealer_final_game == "twopairs":
    user_final_game = "draw"
    dealer_final_game = "draw"
    print("It´s a tie, two pairs for both, the dealer and you")
elif user_final_game == "twopairs":
    user_final_game = "winner"
    print("You win with two pairs")
elif dealer_final_game == "twopairs":
    dealer_final_game = "winner"
    print("Bad luck, the dealer wins with two pairs")
elif user_final_game == "pair" and dealer_final_game == "dealerpair":
    user_final_game = "draw"
    dealer_final_game = "draw"
    print("The dealer and you have only a pair, it´s a tie")
elif user_final_game == "pair":
    user_final_game = "winner"
    print("You win with a pair")
elif dealer_final_game == "dealerpair":
    dealer_final_game = "winner"
    print("The dealer wins wih a pair")
else:
    print("No one wins")

if dealer_final_game == "winner":
    print(f"You lost ${final_bet}")
elif user_final_game == "winner":
    print(f"You earned ${final_bet}")
else:
    print(f"You did not lose any money")


# In[ ]:




