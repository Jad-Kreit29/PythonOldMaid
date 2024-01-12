# Family name: Kreit
# Student number: 300363410
# Course: IT1 1120
# Assignment Number: 4 Part 2
# Year: 2023


# In this implementation a card (that is not a 10) is represented
# by a 2 character string, where the 1st character represents a rank and the 2nd a suit.
# Each card of rank 10 is represented as a 3 character string, first two are the rank and the 3rd is a suit.

import random

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') # remove a queen as the game requires
    return deck

def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)

#####################################

def deal_cards(deck):
     '''(list of str)-> tuple of (list of str,list of str)

     Returns two lists representing two decks that are obtained
     after the dealer deals the cards from the given deck.
     The first list represents dealer's i.e. computer's deck
     and the second represents the other player's i.e user's list.
     '''
     dealer=[]
     other=[]

     # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE

     # Simply add half of the deck to each player
     dealer = dealer + deck[0::2]
     other = other + deck[1::2]

     return (dealer, other)
 


def remove_pairs(l):
    '''
     (list of str)->list of str

     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled

     Precondition: elements of l are cards represented as strings described above

     Testing:
     Note that for the individual calls below, the function should
     return the displayed list but not necessarily in the order given in the examples.

     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    no_pairs=[]
    
    sorted_hand = []

    temp_list = []

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE

    # Sort the given hand before working with it
    sorted_hand = sorted(l)

    # Loop through every element within the hand
    for i in range(len(sorted_hand) - 1):

        # If the character is equal to the next character
        if sorted_hand[i + 1][0:len(sorted_hand[i + 1]) - 1] == sorted_hand[i][0:len(sorted_hand[i]) - 1]:
            # Add the current character to the temp_list
            temp_list.append(sorted_hand[i])

        # When we reach a new set of character
        else:
            # Add the last character in that set
            temp_list.append(sorted_hand[i])

            # If there is only 1 set of characters
            if len(temp_list) == 1:
                # Simply add the one character and rest
                no_pairs = no_pairs + temp_list
                temp_list = []

            # If the total number of characters in the set are odd
            elif (len(temp_list) % 2 != 0):
                # Remove the total number of character - 1 from the temp list
                for j in range(len(temp_list) - 1):
                    temp_list.pop(j)
                # Add to the final list and rest
                no_pairs = no_pairs + temp_list
                temp_list = []

            # If the total number of character in the set are even
            elif (len(temp_list) % 2 == 0):
                # Add nothing. Reset list
                temp_list = []
    


    # If the last character is NOT equal to the one before it
    if sorted_hand[len(sorted_hand) - 1][0:len(sorted_hand[len(sorted_hand) - 1]) - 1] != sorted_hand[len(sorted_hand) - 2][0:len(sorted_hand[len(sorted_hand) - 2]) - 1]:        
        # Add the last character to the FINAL list
        no_pairs.append(sorted_hand[len(sorted_hand) - 1])

    # Else, if the last character IS equal to the ones before it
    else:
        # Add the last character to the list
        temp_list.append(sorted_hand[len(sorted_hand) - 1])

        # Run through the check of the temp_list like before

        # If there is only 1 set of characters
        if len(temp_list) == 1:
            # Simply add the one character and rest
            no_pairs = no_pairs + temp_list
            temp_list = []

        # If the total number of characters in the set are odd
        elif (len(temp_list) % 2 != 0):
            # Remove the total number of character - 1 from the temp list
            for j in range(len(temp_list) - 1):
                temp_list.pop(j)
            # Add to the final list and rest
            no_pairs = no_pairs + temp_list
            temp_list = []

        # If the total number of character in the set are even
        elif (len(temp_list) % 2 == 0):
            # Add nothing. Reset list
            temp_list = []

    random.shuffle(no_pairs)
    return no_pairs



def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE

    # Loop through every element in the given hand/deck
    for item in deck:
        # For every item in the given hand/deck, print them out in one line
        print(item + " ", end=" ")


    
def get_valid_input(n):
     '''
     (int)->int
     Returns an integer given by the user that is at least 1 and at most n.
     Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
     
     Precondition: n>=1
     '''

     # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE

     # Create flag to check user's answer
     flag = True

     # Ask the user for the correct value
     answer = int(input("Give me an integer between 1 and " + str(n) + ": "))

     while flag:
         # If the user inputs the incorrect response
        if ((answer < 1) or (answer > n)):
            # Ask for the correct number again!
            answer = int(input("Invalid number. Please enter integer between 1 and " + str(n) + ": "))
        else:
            flag = False
            return answer

def play_game():
     '''()->None
     This function plays the game'''
    
     deck=make_deck()
     shuffle_deck(deck)
     tmp=deal_cards(deck)

     dealer=tmp[0]
     human=tmp[1]

     print("Hello. My name is Robot and I am the dealer.")
     print("Welcome to my card game!")
     print("Your current deck of cards is:")
     print_deck(human)
     print("\nDo not worry. I cannot see the order of your cards")

     print("Now discard all the pairs from your deck. I will do the same.")
     wait_for_player()
     
     dealer=remove_pairs(dealer)
     human=remove_pairs(human)

     # COMPLETE THE play_game function HERE

     # Set up boolean to check if the game is over
     game_over = False

     # Make variables to track whose turn it is
     player_turn = 0

     # Enter a while loop that continues until the game is won
     while game_over != True:
         
        print("***********************************************************\n")

        # Check to see if the game is over
        # If robot wins
        if (len(human) == 0):
            print("Ups. You do not have any more cards")
            print("Congratulations! You, Human, win.")
            game_over = True
        # If human wins
        elif (len(dealer) == 0):
            print("Ups. I do not have any more cards")
            print("You lost! I, Robot, win.")
            game_over = True
        
        # If the game is not over, play!
        else:
            # If it's the player's turn
            if (player_turn == 0):
                print("Your turn.\n\nYour current deck of cards is:\n")
                
                # Print player's deck after pairs are removed
                print_deck(human)

                # Print message to let user choose computer's card
                print("\n\nI have " + str(len(dealer)) + " cards. If 1 stands for my first card and")
                print(str(len(dealer)) + " for my last card, which of my cards would you like?")

                # Run the get_valid_input function to check if the user gives the right range
                player_choice = get_valid_input(len(dealer))

                # Display proper grammar based on choice
                if(player_choice == 1):
                    print("You asked for my " + str(player_choice) + "st card")
                elif(player_choice == 2):
                    print("You asked for my " + str(player_choice) + "nd card")
                elif(player_choice == 3):
                    print("You asked for my " + str(player_choice) + "rd card")
                else:
                    print("You asked for my " + str(player_choice) + "th card")
                
                # Display the chosen card from the computer, and remove that card from the computer's hand
                print("Here it is. It is " + dealer[player_choice - 1])

                print("\nWith " + dealer[player_choice - 1] + " added, your current deck of cards is:\n")

                # Add the chosen card to the player's hand and print it
                human.append(dealer[player_choice - 1])
                print_deck(human)

                # Discard any pairs, and print the new hand
                print("\n\nAnd after discarding pairs and shuffling, your deck is:\n")
                human = remove_pairs(human)
                print_deck(human)

                # Blank space for looks
                print()

                # Make sure to now remove the chosen card from the robot's hand
                dealer.pop(player_choice - 1)

                # Set the player's turn to the computer, and wait for player input
                player_turn = player_turn + 1
                wait_for_player()
            
            # If it's computer's turn
            elif (player_turn == 1):
                print("My turn.\n")

                # The computer must decide which card to take from our hand randomly
                comp_choice = random.randint(1, len(human))

                # Display proper grammar based on choice
                if(comp_choice == 1):
                    print("I took your " + str(comp_choice) + "st card")
                elif(comp_choice == 2):
                    print("I took your " + str(comp_choice) + "nd card")
                elif(comp_choice == 3):
                    print("I took your " + str(comp_choice) + "rd card")
                else:
                    print("I took your " + str(comp_choice) + "th card")
                
                # Add the chosen card to the computer's hand
                dealer.append(human[comp_choice - 1])

                # Remove the pairs from the computer's hand
                dealer = remove_pairs(dealer)

                # Remove from human's hand
                human.pop(comp_choice - 1)

                # Set the turn to the user, and wait for player's input
                player_turn = player_turn - 1
                wait_for_player()
	 

# main
play_game()
