import random
import os
#returns a random card-->
"""returns a random card from the deck."""
def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card


"""Fuction to calculate score"""
def calculate_score(cards):
    #blackjack condition
    if 11 in cards and 10 in cards and len(cards) == 2:
        #"if sum(cards) == 21 and len(cards) == 2:" will work the same
        return 0
    if 11 in cards and sum(cards) > 21:
        #condition in which we will consider ace not as 11 but as 1
        cards.remove(11)
        cards.append(1)
    return sum(cards)


"""Compare Fuction"""
def compare(userScore,computerScore):
    if computerScore == userScore:
        print("Draw")
    elif computerScore == 0:
        print("You lost the opponent has a Blackjack😢")
    elif userScore == 0:
        print("You won with a Blackjack😎")
    elif userScore > 21 :
        print("You went over, You Lose🤣")
    elif computerScore > 21:
        print("Opponent went over, You win😁")
    elif computerScore < userScore:
        print("You Won -- 🫡")
    else:
        print("You Lose -- 🤐")


def play():
    logo = """
    .------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
    `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
        |  \/ K|                            _/ |                
        `------'                           |__/           
    """
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False
    for _ in range(2):
        new_card=deal_card()
        #+= and extends works the same but we cannot use them here,
        #as they are used to add another list to the existing list
        #if you want to add a single object you will have to the list
        #then use the append function.
        user_cards.append(new_card)
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" Your cards:{user_cards},current score:{user_score}")
        #because dealer is supposed to reveal it's first card
        print(f" Computer's first cards:{computer_cards[0]}")

        #if computer or user has a blackjack(0) or if the user's score is over 21, then end the game:
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            play_again = input("Type 'y' to get another card, type 'n' to pass: ")
            if play_again == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True


    #if the user is done then, the computer should make it's own move if the 
    #score of the computer is less then 17 and is not a blckjack(0) condition
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"  Your final hand:{user_cards},final score:{user_score}")
    print(f"  Computer's final hand:{computer_cards},final score:{computer_score}")

    print(compare(user_score,computer_score))


while input("Do you want to play a game of BlackJack -- ") == "y":
    os.system('cls')
    play()