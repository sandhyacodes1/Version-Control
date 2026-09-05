import random

def deal_card():
    #Returns a random card from the deck.
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    #Take a list of cards and return the score calculated from the cards
    # Check for blackjack (ace + 10 with only 2 cards)
    if len(cards) == 2 and sum(cards) == 21:
        return 0  # 0 represents a blackjack
    
    # Handle Ace (11) if score goes over 21
    if sum(cards) > 21 and 11 in cards:
        # Replace 11 with 1
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare(user_score, computer_score):
    #Compare user and computer scores and return the result
    if user_score == computer_score:
        return "It's a draw!"
    elif computer_score == 0:
        return "Computer has a Blackjack! You lose!"
    elif user_score == 0:
        return "You have a Blackjack! You win!"
    elif user_score > 21:
        return "You went over 21! You lose!"
    elif computer_score > 21:
        return "Computer went over 21! You win!"
    elif user_score > computer_score:
        return "You win! "
    else:
        return "You lose!"

def play_game():
    #Main game function
    print("\n" + "="*50)
    print("BLACKJACK")
    print("="*50)
    
    # Deal initial cards
    user_cards = []
    computer_cards = []
    is_game_over = False
    
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        
        print(f"\nYour cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        
        # Check for game ending conditions
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # Ask user if they want another card
            another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if another_card == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
    
    # Computer's turn - draws cards until score >= 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    # Final scores
    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print("\n" + "="*50)
    print(compare(user_score, computer_score))
    print("="*50)

# Main game loop
print("Welcome to Blackjack!")
while True:
    play_again = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play_again == "y":
        # Clear the console
        print("\n" * 100)
        play_game()
    elif play_again == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid input! Please type 'y' or 'n'.")