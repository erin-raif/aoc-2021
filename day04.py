# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 10:48:12 2021

@author: eraif
"""
import numpy as np

def read_file(filename):
    f = open(filename, 'r')
    # Dump all contents
    contents = []
    for line in f:
        contents.append(line.strip('\n'))
    # Get bingo numbers and bingo cards
    numbers = contents[0].split(',')
    numbers = [int(n) for n in numbers]
    contents.pop(0)
    contents = [y for y in contents if y != ""]
    cards = [[]]
    i = 0
    for l in contents:
        l = l.split(' ')
        l = [int(i) for i in l if i != ""]
        cards[-1].append(l)
        if i % 5 == 4:
            cards.append([])
        i += 1
    cards.pop(-1)
    # Create transposed version of cards to save looping time later
    trans_cards = []
    for card in cards:
        trans_cards.append(list(map(list, zip(*card))))
    return numbers, cards, trans_cards

def check_rows(card, called):
    """Check row for bingo"""
    for row in card:
        if all(x in called for x in row):
            return True
    return False

def check_card(card, trans_card,called):
    """ Check card for bingo."""
    if check_rows(card,called):
        return True
    elif check_rows(trans_card,called):
        # Effectively check columns
        return True
    else:
        return False

def check_all_cards(cards, trans_cards, called):
    """ Check every card for bingo.
        If one bingoes, cut loop and return index of card.
        Otherwise, return -1."""
    for i in range(len(cards)):
        if check_card(cards[i], trans_cards[i], called):
            return i
    return -1

def calculate_score(card, called):
    card_numbers = [item for sublist in card for item in sublist]
    for number in called:
        if number in card_numbers:
            card_numbers.remove(number)
    uncalled_total = np.sum(np.array(card_numbers))
    score = uncalled_total * called[-1]
    return score  

def part_one(numbers, cards, trans_cards):
    """ Find winning bingo card """
    called = numbers[:5]
    i = 5 # Cannot have bingo with less than 5 numbers, reduce looping
    finished = False

    while i < len(numbers) and not finished:
        winning_card = check_all_cards(cards, trans_cards, called)
        if winning_card != -1:
            # If a winner is found, calculate score
            print("Part 1:", calculate_score(cards[winning_card], called))
            finished = True # Unnecessary now in function but can't be bothered to change
        else:
            called.append(numbers[i])
            i += 1
    return     

def part_two(numbers, cards, trans_cards):
    """ Find the losing bingo card """
    called = numbers[:5]
    i = 5 # Cannot have bingo with less than 5 numbers, reduce looping
    finished = False
    while i < len(numbers) and not finished:
        winning_card = check_all_cards(cards, trans_cards, called)
        if winning_card != -1:
            # If a winner is found, remove it from the list if there are multiple cards in the list
            if len(cards) > 1:
                cards.pop(winning_card)
                trans_cards.pop(winning_card)
            elif len(cards) == 1:
                finished = True # Unnecessary now in function but can't be bothered to change
        else:
            called.append(numbers[i])
            i += 1
    print("Part 2:", calculate_score(cards[0], called))
    return

numbers, cards, trans_cards = read_file('day04.txt')
part_one(numbers, cards, trans_cards)
part_two(numbers, cards, trans_cards)