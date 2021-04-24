path = "../test_data/B.dat"

A = []
with open(path) as f:
    s = [s.strip() for s in f.readlines()]
    A = [numbers.split(" ") for numbers in s[:3]]
    called = s[4:]


import numpy as np
np_card = np.array(A, dtype=np.int32)

def checked_card(card, numbers):
    tmp_card = np.full((3, 3), False)
    for number in numbers:
        tmp_card = np.logical_or(tmp_card, card == int(number))
    return tmp_card

def bingo_or_not(booled_card):
    if booled_card[0][0] and booled_card[0][1] and booled_card[0][2]:
        return "Yes" 
    if booled_card[1][0] and booled_card[1][1] and booled_card[1][2]:
        return "Yes" 
    if booled_card[2][0] and booled_card[2][1] and booled_card[2][2]:
        return "Yes" 
    if booled_card[0][0] and booled_card[1][0] and booled_card[2][0]:
        return "Yes" 
    if booled_card[0][1] and booled_card[1][1] and booled_card[2][1]:
        return "Yes" 
    if booled_card[0][2] and booled_card[1][2] and booled_card[2][2]:
        return "Yes" 
    if booled_card[0][0] and booled_card[1][1] and booled_card[2][2]:
        return "Yes" 
    if booled_card[0][2] and booled_card[1][1] and booled_card[2][0]:
        return "Yes" 
    return "No"

print(bingo_or_not(checked_card(np_card, called)))
