# importing necessary common utils and packages
import os
from pathlib import Path
import datetime as dt
from itertools import product

# defining varibales to be used for industrialization
odate = dt.datetime.today().strftime("%Y-%m-%d")
project_name = "knights_algorithm"
version = "knights_algorithm_final_script"

#  relative paths often cause file read/write errors. Always start from project_root variable to avoid time loss in resolving path errors
current_file_directory = os.path.abspath(__file__)
project_root_directory = current_file_directory[:-26]
project_root = Path(os.path.dirname(project_root_directory))

# set path for data and result folder
data_folder = project_root / "data"
result_folder = project_root / "result"

# Map each element of the keypad to a coordinate that reflects the relative position of the keys
keypad = {
    "A": (0, 0),
    "B": (0, 1),
    "C": (0, 2),
    "D": (0, 3),
    "E": (0, 4),
    "F": (1, 0),
    "G": (1, 1),
    "H": (1, 2),
    "I": (1, 3),
    "J": (1, 4),
    "K": (2, 0),
    "L": (2, 1),
    "M": (2, 2),
    "N": (2, 3),
    "O": (2, 4),
    "1": (3, 1),
    "2": (3, 2),
    "3": (3, 3),
}

# Define the identification of the constraint: vowels on the keypad
vowels = {"A", "E", "I", "O"}


# function for calculating all the valid knight moves
def knight_moves():
    """Generate all possible knight moves by manipulating the x and y coordinates"""
    moves = list(product([1, -1], [2, -2])) + list(product([2, -2], [1, -1]))
    return moves


# function for calculating the possible knight moves for a certain key
def knight_moves_options(key):
    """Generate valid knight moves for specific key by manipulating the x and y coordinates"""
    x, y = keypad[key]
    key_all_moves = []
    for x_shift, y_shift in knight_moves():
        new_x, new_y = x + x_shift, y + y_shift
        for valid_new_key, (valid_new_x, valid_new_y) in keypad.items():
            if valid_new_x == new_x and valid_new_y == new_y:
                key_all_moves.append(valid_new_key)
    return key_all_moves


# Memoization cache to store intermediate results
memo = {}


# recursive function to find all possible sequences
def find_sequences(current_key, length, vowel_count):
    """Generate sequences for the knight move recursively by keeping track of the current sequence and number of vowels used"""

    # check for 10 key sequences and stop checking for further keys
    if length == 10:  # Base case: sequence of length 10
        return 1

    # using Memoization for early stopping to avoid checks on repeated sequences
    if (current_key, length, vowel_count) in memo:
        return memo[(current_key, length, vowel_count)]

    total_sequences = 0
    for move in knight_moves_options(current_key):
        new_vowel_count = vowel_count + (1 if move in vowels else 0)
        if new_vowel_count <= 2:  # Ensure at most 2 vowels in the sequence
            total_sequences += find_sequences(move, length + 1, new_vowel_count)

    memo[(current_key, length, vowel_count)] = total_sequences
    return total_sequences


# function to loop through all keys
def generate_knight_sequences():
    """Looping through all unique keys on keypad"""
    total_count = 0
    for key in keypad:
        initial_vowel_count = 1 if key in vowels else 0
        total_count += find_sequences(key, 1, initial_vowel_count)
    return total_count


# Call the function to count and print valid sequences
valid_sequences_count = generate_knight_sequences()
print("Total Valid Sequences:", valid_sequences_count)
with open(result_folder / r"knights_algorithm_10_sequences_final.txt", "w") as fo:
    fo.write(f"Total number of sequences detected are: {valid_sequences_count} \n\n")
