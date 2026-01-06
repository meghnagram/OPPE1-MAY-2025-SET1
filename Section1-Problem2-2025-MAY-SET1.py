# This mappings can be used as needed.
suit_values = {'S': 1, 'H':2, 'D': 3, 'C': 4}
rank_values = {'A': 1, 'J': 11, 'Q': 12, 'K': 13}


def card_to_value_tuple(card: str) -> tuple:
    '''Converts the card of format "{rank}{suit}" to value tuple.

    The suit values from low to high:

    - `S` (Spades) - 1
    - `H` (Hearts) - 2
    - `D` (Diamonds) - 3
    - `C` (Clubs) - 4

    The rank values from low to high:

    - `A` (Ace) - 1
    - `2` through `10` - same as the number
    - `J` (Jack) - 11
    - `Q` (Queen) - 12
    - `K` (King) - 13

    Examples:
    >>> card_to_value_tuple('AH')
    (2, 1)
    >>> card_to_value_tuple('7D')
    (3, 7)
    >>> card_to_value_tuple('QS')
    (1, 12)
    >>> card_to_value_tuple('9C')
    (4, 9)
    >>> card_to_value_tuple('10D')
    (3, 10)

    Args:
        card1 (str): A valid card string (e.g., "AH", "7D")
        card2 (str): Another valid card string

    Returns:
        str: The higher-value card
    '''
    
    
    suit, rank = card[-1:], card[:-1]
    return (
      suit_values[suit],
      rank_values[rank] if rank in rank_values else int(rank)
    )

#Another Method:

# # This mappings can be used as needed.
# suit_values = {'S': 1, 'H':2, 'D': 3, 'C': 4}
# rank_values = {'A': 1, 'J': 11, 'Q': 12, 'K': 13}


# def card_to_value_tuple(card: str) -> tuple:
   
#     suit=card[-1]
#     rank=card[0:-1:]
    
#     suit_value = suit_values[suit]
#     rank_value = rank_values[rank] if rank in rank_values.keys() else int(rank)
    
#     return (suit_value,rank_value)


# Card to Value Tuple
# Write a function card_to_value_tuple that takes in a playing card of as a string of format '{rank}{suit}' and returns a tuple of integers format (suit_value, rank_value) as described below.

# The suit values from low to high:

# S (Spades) - 1
# H (Hearts) - 2
# D (Diamonds) - 3
# C (Clubs) - 4
# The rank values from low to high:

# A (Ace) - 1
# 2 through 10 - same as the number
# J (Jack) - 11
# Q (Queen) - 12
# K (King) - 13

# Example

# >>> card_to_value_tuple('AH')
# (2, 1)
# >>> card_to_value_tuple('7D')
# (3, 7)
# >>> card_to_value_tuple('QS')
# (1, 12)
# >>> card_to_value_tuple('9C')
# (4, 9)
# >>> card_to_value_tuple('10D')
# (3, 10)

    
