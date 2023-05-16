def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.
    
    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21
    
    Hands are represented as a list of cards. Each card is represented by a string.
    
    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.
    
    When determining a hand's total, you should try to count aces in the way that 
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.
    
    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    def get_num(string):
        if string in ('J', 'Q', 'K'):
            return 10
        if string == 'A':
            return 11
        return int(string)
    
    def get_hand_num(hand):
        list_num = [get_num(x) for x in hand]
        num_aces = len([x for x in list_num if x >= 11])
        total_sum = sum([x for x in list_num if x < 11])
        total_sum = total_sum + num_aces
        while total_sum + 10 <= 21 and num_aces > 0:
            total_sum += 10
            num_aces -= 1
        return total_sum
    
    suma_hand_1 = get_hand_num(hand_1)
    suma_hand_2 = get_hand_num(hand_2)
    return suma_hand_1 <= 21 and (suma_hand_1 > suma_hand_2 or suma_hand_2 > 21)       
  
    pass

print(blackjack_hand_greater_than(['K'], ['3', '4']))
print(blackjack_hand_greater_than(['K'], ['10']))
print(blackjack_hand_greater_than(['K', 'K', '2'], ['3']))