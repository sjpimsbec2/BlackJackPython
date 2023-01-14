import random

# Function to get a random card value between 1 and 11
def get_card():
    # list of cards are 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11
    # 11 is an ace
    # 10 is a jack, queen, king
    # 2-10 are their respective values
    card_value = random.randint(2, 11)
    return card_value

# Function to check if the hand is a blackjack (21)
def check_blackjack(hand):
    if hand == 21:
        return True
    else:
        return False

# Function to calculate the score of a hand, taking into account any aces (11) that would make the score over 21
def calculate_score(hand):
    score = 0
    # Add up the score of the hand
    for card in hand:
        score += card
    if score > 21:
        for card in hand:
            # If the card is an ace, change it to a 1 and recalculate the score
            if card == 11:
                score -= 10
                break
    return score

# Function to ask the user if they want to play again
def play_again():
    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    return choice.lower() == "y"

# Main game loop
def when_user_type_no(user_hand, computer_hand, user_score, computer_score):
    if computer_score > 21:
        final_score_card(calculate_score, user_hand, computer_hand)
        print("Opponent went over. You win! 😁")        
    elif user_score > computer_score:
        final_score_card(calculate_score, user_hand, computer_hand)
        print("You win! 😁")       
    elif user_score < computer_score:
        final_score_card(calculate_score, user_hand, computer_hand)
        print("You Lose! 😢")  
    else:
        final_score_card(calculate_score, user_hand, computer_hand)
        print("It's a draw! 😐")

def final_score_card(calculate_score, user_hand, computer_hand):
    print("\tYour final cards: ", user_hand, "final score: ", calculate_score(user_hand))
    print("\tComputer's final cards: ", computer_hand, "final score: ", calculate_score(computer_hand))

def current_score_cards(calculate_score, user_hand, computer_hand):
    print("\tYour cards: ", user_hand, "current score: ", calculate_score(user_hand))
    print("\tComputer's first card is: ", computer_hand[0])

def main():
    while True:
        # Deal the initial hands to the user and computer
        user_hand = [get_card(), get_card()]
        computer_hand = [get_card(), get_card()]

        # Check if either the user or computer has a blackjack
        user_blackjack = check_blackjack(calculate_score(user_hand))
        computer_blackjack = check_blackjack(calculate_score(computer_hand))

        # Determine the result if both have blackjack or just one of them
        if user_blackjack and computer_blackjack:
            final_score_card(calculate_score, user_hand, computer_hand) 
            print("It's a draw!")
        elif user_blackjack:
            final_score_card(calculate_score, user_hand, computer_hand) 
            print("You win! You have a blackjack.")
        elif computer_blackjack:
            final_score_card(calculate_score, user_hand, computer_hand) 
            print("You lose! The computer has a blackjack. 😭")
        else:
            # Reveal the computer's first card and the user's cards
            current_score_cards(calculate_score, user_hand, computer_hand)
            # Allow the user to draw cards until they choose to stop or they go over 21
            while True:
                user_choice = input("Type 'y' to get another card, type 'n' to pass: ")
                if user_choice.lower() == "y":
                    user_hand.append(get_card())
                    user_score = calculate_score(user_hand)
                    if user_score > 21:
                        final_score_card(calculate_score, user_hand, computer_hand)
                        print("You lose! You went over 21.")
                        break
                    else:
                        current_score_cards(calculate_score, user_hand, computer_hand)                   
                else:             

            # Let the computer draw cards until their score is over 16
                    while calculate_score(computer_hand) <= 16:
                        computer_hand.append(get_card())

                    # Calculate the final scores and determine the winner
                    user_score = calculate_score(user_hand)
                    computer_score = calculate_score(computer_hand)                
                    when_user_type_no(user_hand, computer_hand, user_score, computer_score)
                    break
        if not play_again():
            break
if __name__ == "__main__":
    main()
