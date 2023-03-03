import random

# create a deck with 52 poker
def get_shuffled_deck():

    suits = {'♣', '♠', '♦', '♥'}
    ranks = {'2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'}
    deck = []

    for suit in suits:
        for rank in ranks:
            deck.append(suit + ' ' + rank)
    random.shuffle(deck)
    return deck

# deal a card to participant
def deal_card(deck, participant):
    card = deck.pop()
    participant.append(card)
    return card

# calculates and returns the sum of a hand
def compute_total(hand):
    values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':11}
    result = 0 # the sum of a cards
    numAces = 0 # number of A

    # compute the total and number of A
    for card in hand:
        result += values[card[2:]]
        if card[2] == 'A':
            numAces += 1
    
    # if the result is bigger than 21, cauculate A as 1
    while result > 21 and numAces > 0:
        result -= 10
        numAces -= 1
    return result

def print_hand(hand):
    for i in range(len(hand)):
        print(hand[i], end = '  ')
    print()

# if there is no A in initial hand
def hard(hand, b_f_card, deck, double_bool):
    values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':11}
    init = 1

    while True:
        if compute_total(hand) >= 17:
            return

        elif compute_total(hand) >= 13 and compute_total(hand) <= 16:
            if values[b_f_card[2:]] <= 6:
                return

            else:
                deal_card(deck, hand)
                init = 0
                print("Player's hand："); print_hand(hand)
                if compute_total(hand) > 21:
                    print('Player exceeding 21')
                    return

        elif compute_total(hand) == 12:
            if values[b_f_card[2:]] == 2 or values[b_f_card[2:]] == 3 or values[b_f_card[2:]] >= 7:
                deal_card(deck, hand)
                init = 0
                print("Player's hand："); print_hand(hand)
                if compute_total(hand) > 21:
                    print('Player exceeding 21')
                    return
            else:
                return

        elif compute_total(hand) == 11:
            if init == 1:
                double_bool[0] = 1
            deal_card(deck, hand)
            init = 0
            print("Player's hand："); print_hand(hand)
            if compute_total(hand) > 21:
                print('Player exceeding 21')
                return

        elif compute_total(hand) == 10:
            if values[b_f_card[2:]] <= 9:
                if init == 1:
                    double_bool[0] = 1
                deal_card(deck, hand)
                init = 0
                print("Player's hand："); print_hand(hand)
                if compute_total(hand) > 21:
                    print('Player exceeding 21')
                    return
            else:
                deal_card(deck, hand)
                init = 0
                print("Player's hand："); print_hand(hand)
                if compute_total(hand) > 21:
                    print('Player exceeding 21')
                    return

        elif compute_total(hand) == 9:
            if values[b_f_card[2:]] >= 3 and values[b_f_card[2:]] <= 6:
                if init == 1:
                    double_bool[0] = 1
                deal_card(deck, hand)
                init = 0
                print("Player's hand："); print_hand(hand)
                if compute_total(hand) > 21:
                    print('Player exceeding 21')
                    return
            else:
                deal_card(deck, hand)
                init = 0
                print("Player's hand："); print_hand(hand)
                if compute_total(hand) > 21:
                    print('Player exceeding 21')
                    return

        else:
                deal_card(deck, hand)
                init = 0
                print("Player's hand："); print_hand(hand)
                if compute_total(hand) > 21:
                    print('Player exceeding 21')
                    return            


                                                         


        



# if there is A in initial hand
def soft(hand, b_f_card, deck, double_bool):
    values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':11}
    init = 1

    while True:    
        if compute_total(hand) >= 20:
            return

        elif compute_total(hand) == 19:
            if values[b_f_card[2:]] == 6:
                if init == 1:
                    double_bool[0] == 1
                return
            else:
                return

        elif compute_total(hand) == 18:
            if values[b_f_card[2:]] <= 6:
                if init == 1:
                    double_bool[0] == 1
                return
            elif values[b_f_card[2:]] >= 9:
                deal_card(deck, hand)
                init = 0
                print("Player's hand："); print_hand(hand)
                if compute_total(hand) > 21:
                    print('Player exceeding 21')
                return
            else:
                return

        elif compute_total(hand) == 17:
            if values[b_f_card[2:]] <= 6 and values[b_f_card[2:]] >= 3:
                if init == 1:
                    double_bool[0] == 1
                deal_card(deck, hand)
                init = 0
                print("Player's hand："); print_hand(hand)
                if compute_total(hand) > 21:
                    print('Player exceeding 21')
                return                  
            else:
                deal_card(deck, hand)
                init = 0
                print("Player's hand："); print_hand(hand)
                if compute_total(hand) > 21:
                    print('Player exceeding 21')
                return

        elif compute_total(hand) == 15 or compute_total(hand) == 16:
            if values[b_f_card[2:]] <= 6 and values[b_f_card[2:]] >= 4:
                if init == 1:
                    double_bool[0] == 1
                deal_card(deck, hand)
                init = 0
                print("Player's hand："); print_hand(hand)
                if compute_total(hand) > 21:
                    print('Player exceeding 21')
                return                  
            else:
                deal_card(deck, hand)
                init = 0
                print("Player's hand："); print_hand(hand)
                if compute_total(hand) > 21:
                    print('Player exceeding 21')
                return

        elif compute_total(hand) <= 14:
            if values[b_f_card[2:]] <= 6 and values[b_f_card[2:]] >= 5:
                if init == 1:
                    double_bool[0] == 1
                deal_card(deck, hand)
                init = 0
                print("Player's hand："); print_hand(hand)
                if compute_total(hand) > 21:
                    print('Player exceeding 21')
                return                  
            else:
                deal_card(deck, hand)
                init = 0
                print("Player's hand："); print_hand(hand)
                if compute_total(hand) > 21:
                    print('Player exceeding 21')
                return                                                                        


def blackjack():
    # start with 100 wager
    wager = 100

    con = "y"
    win_count = 0
    count = 0

    while con in ('', "y", "Y"):
        player_ex = 0
        banker_ex = 0
        double_bool = [0]

        deck = get_shuffled_deck()
        house = [] # banker's hand
        player = [] # player's hand
    
        # deal 2 cards to player and banker
        for i in range(2):
            deal_card(deck, player)
            deal_card(deck, house)
        
        # print hand
        print("Banker's first card: "); print(house[0])
        print("Player's initial hand："); print_hand(player)

        # AI action
        a_in_hand = 0
        for i in range(2):
            if player[i][2:] == 'A':
                a_in_hand = 1

        if a_in_hand == 1:
            soft(player, house[0], deck, double_bool)
            if compute_total(player) > 21:
                player_ex = 1
        else:
            hard(player, house[0], deck, double_bool)
            if compute_total(player) > 21:
                player_ex = 1
        if double_bool[0] == 1:
            print("Double!")

        # The banker decides whether to take a card according to the dealer's rule
        if player_ex != 1 and compute_total(house) < 17:
            while compute_total(house) < 17:
                card = deal_card(deck, house)
                print("Banker's hand："); print_hand(house)

                if compute_total(house) > 21:
                    print('Banker exceeding 21!')
                    banker_ex = 1
        elif player_ex != 1:
            print("Banker's hand："); print_hand(house)            


        # calculate banker and player's points respectively
        # compare points, output winning and losing result information and wager
        houseTotal, playerTotal = compute_total(house), compute_total(player)
    
        if player_ex == 1:
            if double_bool[0] == 1:
                wager -= 20
            else:
                wager -= 10
            player_ex = 0
            count += 1
            print('Banker Win!')
            print("Wager: " + str(wager))
            print("wining number:" + str(win_count))
            print("number of bets:" + str(count))             
        elif banker_ex == 1:
            if double_bool[0] == 1:
                wager += 20
            else:
                wager += 10            
            banker_ex = 0
            win_count += 1
            count += 1
            print('Player Win!')
            print("Wager: " + str(wager))
            print("wining number:" + str(win_count))
            print("number of bets:" + str(count))                                                                 
        elif houseTotal > playerTotal:
            count += 1            
            print('Banker win!')
            if double_bool[0] == 1:
                wager -= 20
            else:
                wager -= 10
            print("Wager: " + str(wager))
            print("wining number:" + str(win_count))
            print("number of bets:" + str(count))                     
        elif houseTotal < playerTotal:
            if double_bool[0] == 1:
                wager += 20
            else:
                wager += 10
            win_count += 1
            count += 1                     
            print('Player Win!')
            print("Wager: " + str(wager))
            print("wining number:" + str(win_count))
            print("number of bets:" + str(count))                                 
        elif houseTotal == 21 and 2 == len(house) < len(player) : # Banker win if it has blackjack
            if double_bool[0] == 1:
                wager -= 20
            else:
                wager -= 10
            count += 1                
            print('Banker Win!')
            print("Wager: " + str(wager))
            print("wining number:" + str(win_count))
            print("number of bets:" + str(count))                                 
        elif playerTotal == 21 and 2 == len(player) < len(house) : # Player win if it has blackjack
            if double_bool[0] == 1:
                wager += 20
            else:
                wager += 10
            win_count += 1
            count += 1                     
            print('Player Win!')
            print("Wager: " + str(wager))
            print("wining number:" + str(win_count))
            print("number of bets:" + str(count))                     
        else:
            print('Tie!')
            print("Wager: " + str(wager))
        
        con = input("Do you want to continue? (y/n)  ")

blackjack()