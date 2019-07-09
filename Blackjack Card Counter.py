from IPython.display import clear_output

class rules():
    """
    
    Online Blackjack Rules
    ----------------------
    Blackjack Pays 3:2
    Insurance Pays 2:1
    Dealer Must Hit Soft 17
    Double Any Two Cards
    Split Up To 3 Hands
    1 Card Dealt On Split Aces
    6 Decks


    Card Counter App Help
    ---------------------
    Type 'Stop' to exit
    Type 'Restart' to rerun program from beginning 
    Type 'Help' for Blackjack rules and app help
    Type 'Decks' to change the number of decks in play (Default = 6)
    Enter each card value as it appears in the input prompt: '>>'

    *** When the true count climbs above 1.0, the odds move in favor of the player


     Acceptable |  Card 
    Card Inputs | Values
    ---------------------
            '2' | 1
            '3' | 1
            '4' | 1
            '5' | 1
            '6' | 1
            '7' | 0
            '8' | 0
            '9' | 0
            '0' | -1 (Use '0' for 10)
            'J' | -1
            'Q' | -1
            'K' | -1
            'A' | -1

    """

def main():

    CARD_VALUES = {
            '2': 1,
            '3': 1,
            '4': 1,
            '5': 1,
            '6': 1,
            '7': 0,
            '8': 0,
            '9': 0,
            '0': -1, # use '0' for 10 to keep everything a single character
            'J': -1,
            'Q': -1,
            'K': -1,
            'A': -1,
            }

    DECKS = 6
    VALUES = ['2','3','4','5','6','7','8','9','0','J','Q','K','A','j','q','k','a']
    
    count = 0
    cards = 0
    user_input = True
    decks_played = 0
    
    print('\033[1m' + "Blackjack Card Counter")
    print("----------------------")
    print('\033[0m' + 'Enter each card value as it appears.')
    print('When the true count climbs above 1.0, the odds move in favor of the player')
    print()
    print('Type \'Stop\' to exit the program')
    print('Type \'Restart\' to rerun the program from beginning ')
    print('Type \'Help\' for Blackjack rules and app help')
    print('Type \'Decks\' to change the number of decks in play (Default = 6)')
    print()


    while user_input:
        
        while True:
            user_input = input(">> ")

            #Help
            if user_input == 'Help' or user_input == 'help':
                help(rules)
                continue

            #Stop
            if user_input == 'Stop' or user_input == 'stop':
                print('Goodbye')
                return

            #Restart   
            if user_input == 'Restart' or user_input == 'restart':
                clear_output()
                count = 0
                cards = 0
                decks_played = 0
                continue
                
            #Decks   
            if user_input == 'Decks' or user_input == 'decks':
                DECKS = int(input('How many decks are in play? '))
                continue
                
            a_set = set(user_input) 
            b_set = set(VALUES) 
            if (a_set & b_set): 
                break 
            print('Invalid input.')

        cards += len(user_input)
        print("Card #:",cards, "out of", DECKS*52)
        for card in user_input:
            count += CARD_VALUES[card.upper()]
        decks_played = cards / 52.0
        true_count = count / (DECKS - decks_played)
        print('Count: {}'.format(count))
        print('True Count: {}'.format(true_count))
        if decks_played >= 1 and decks_played <= 1.25 or decks_played >= 2 and decks_played <= 2.25 or decks_played >= 3 and decks_played <= 3.25 or decks_played >= 4 and decks_played <= 4.25 or decks_played >= 5 and decks_played <= 5.25 or decks_played >= 6 and decks_played <= 6.25:
            print('Decks played: {0:0.0f}'.format(decks_played))

if __name__ == '__main__':
    main()
