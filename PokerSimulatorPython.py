import random
import pandas as pd
import copy
import numpy as np

def create_deck():
    suits = ['S', 'H', 'C', 'D']  # Suits
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]  # Values, with 14 representing Ace
    deck = [[suit, value] for suit in suits for value in values]
    return deck

