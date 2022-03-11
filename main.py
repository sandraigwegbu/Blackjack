#BLACKJACK

################### My Blackjack House Rules ###################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## All available cards have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

########################## Let's Play! #########################

from art import logo
from replit import clear
import random

start_game = input("Do you want to play a game of Blackjack?\nType 'y' or 'n': ").lower()

def blackjack(): #function created for recursion
    your_cards = []
    computer_cards = []
    
    #Define output functions
    def deal_card():
        """Returns a random card from the deck"""
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        random_card = random.choice(cards)
        return random_card
    
    def calculate_score(cards): #input your_cards or computer_cards
        """Takes a list of cards and returns the calculated score"""
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        if 11 in cards and sum(cards) > 21 and cards[0] != 11 and cards[1] != 11:
            cards.remove(11)
            cards.append(1)
        return sum(cards)
    
    #Begin the game...
    if start_game == "y":
        clear()
        print(logo)
    
        for _ in range(2): #computer and user draws first two cards
            your_cards.append(deal_card())
            computer_cards.append(deal_card())
        
        game_over = False
        while game_over == False:
            your_score = calculate_score(your_cards)
            computer_score = calculate_score(computer_cards)
            print(f"Your cards: {your_cards}. Current score: {your_score}.")
            print(f"Computer's first card: [{computer_cards[0]}].")
    
            #if Blackjack or above 21, game over... otherwise make a choice
            if your_score == 0 or computer_score == 0 or your_score > 21:
                game_over = True
            else:
                another_card = input("\nType 'y' to get another card. Type 'n' to pass: ").lower()
                if another_card == "y":
                    print("\n")
                    your_cards.append(deal_card())
                else:
                    game_over = True
        
        #Computer's turn, computer draws as long as score is still below 17
        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)
    
        #Final scores
        print(f"\nYour final hand: {your_cards}. Your final score: {your_score}.")
        print(f"Computer's final hand: {computer_cards}. Computer's final score: {computer_score}.")
    
        #Determine the winner
        def compare(your_score,computer_score):
            """Compares your_score and computer_score and determines outcome of the Blackjack game"""
            if computer_score == 0:
                return "You lose. Computer has Blackjack 😱"
            elif your_score == 0:
                return "You win with a Blackjack 😎"
            elif your_score > 21:
                return "You went over. You lose 😭"
            elif computer_score > 21:
                return "Computer went over. You win 😁"
            elif your_score == computer_score:
                return "It's a draw 🙂"
            elif computer_score > your_score:
                return "Computer wins 😭"
            elif your_score > computer_score:
                return "You win 😁"   
        
        print("\n" + compare(your_score,computer_score))
    
        #Play again?
        new_game = input("\nDo you want to start a new game of Blackjack?\nType 'y' or 'n': ").lower()
    
        if new_game == "y":
            blackjack()

blackjack()