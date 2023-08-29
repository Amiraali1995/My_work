"""def first_non_repeating_char(input_str):
    char_count = {}
    for char in input_str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in input_str:
        if char_count[char] == 1:
            return char
    return None  # If no non-repeating character is found
input_str = "hello"
output = first_non_repeating_char(input_str)
print(output) """
from collections import *
def first_non_repeating_char(input_str):
    char_count = Counter(input_str)

    for char in input_str:
        if char_count[char] == 1:
            return char
    return None  # If no non-repeating character is found
input_str = "hello"
output = first_non_repeating_char(input_str)
print("The first non repeat character is : "+output)