#!/usr/bin/env python
"""
This code codes and decodes a certain word
"""

def break_text(text):                   # Breaks up a text in characters and puts it in a list
    text_list = []
    length_text = len(text)
    for i in range(length_text):
        text_list.append(text[i:i + 1])
    return text_list


def code_text(text): # Changes every character requested to a different one. You can make your own code/decoder here

#Lowercase letters

    if text == "a":
        return "b"
    if text == "b":
        return "c"
    if text == "c":
        return "d"
    if text == "d":
        return "e"
    if text == "e":
        return "f"
    if text == "f":
        return "g"
    if text == "g":
        return "h"
    if text == "h":
        return "i"
    if text == "i":
        return "j"
    if text == "j":
        return "k"
    if text == "k":
        return "l"
    if text == "l":
        return "m"
    if text == "m":
        return "n"
    if text == "n":
        return "o"
    if text == "o":
        return "p"
    if text == "p":
        return "q"
    if text == "q":
        return "r"
    if text == "r":
        return "s"
    if text == "s":
        return "t"
    if text == "t":
        return "u"
    if text == "u":
        return "v"
    if text == "v":
        return "w"
    if text == "w":
        return "x"
    if text == "x":
        return "y"
    if text == "y":
        return "z"
    if text == "z":
        return "a"

#Uppercase letters

    if text == "A":
        return "B"
    if text == "B":
        return "C"
    if text == "C":
        return "D"
    if text == "D":
        return "E"
    if text == "E":
        return "F"
    if text == "F":
        return "G"
    if text == "G":
        return "H"
    if text == "H":
        return "I"
    if text == "I":
        return "J"
    if text == "J":
        return "K"
    if text == "K":
        return "L"
    if text == "L":
        return "M"
    if text == "M":
        return "N"
    if text == "N":
        return "O"
    if text == "O":
        return "P"
    if text == "P":
        return "Q"
    if text == "Q":
        return "R"
    if text == "R":
        return "S"
    if text == "S":
        return "T"
    if text == "T":
        return "U"
    if text == "U":
        return "V"
    if text == "V":
        return "W"
    if text == "W":
        return "X"
    if text == "X":
        return "Y"
    if text == "Y":
        return "Z"
    if text == "Z":
        return "A"
    if text == ",":
        return ":"

#Common punctuation marks

    if text == " ":
        return "="
    if text == "-":
        return "+"
    if text == ".":
        return ">"
    if text == "?":
        return "<"
    if text == "!":
        return "“"

#Numbers

    if text == "0":
        return "1"
    if text == "1":
        return "2"
    if text == "2":
        return "3"
    if text == "3":
        return "4"
    if text == "4":
        return "5"
    if text == "5":
        return "6"
    if text == "6":
        return "7"
    if text == "7":
        return "8"
    if text == "8":
        return "9"
    if text == "9":
        return "0"


def decode_text(text): # Changes every character requested to a different one. You can make your own code/decoder here

#Lowercase letters

    if text == "a":
        return "z"
    if text == "b":
        return "a"
    if text == "c":
        return "b"
    if text == "d":
        return "c"
    if text == "e":
        return "d"
    if text == "f":
        return "e"
    if text == "g":
        return "f"
    if text == "h":
        return "g"
    if text == "i":
        return "h"
    if text == "j":
        return "i"
    if text == "k":
        return "j"
    if text == "l":
        return "k"
    if text == "m":
        return "l"
    if text == "n":
        return "m"
    if text == "o":
        return "n"
    if text == "p":
        return "o"
    if text == "q":
        return "p"
    if text == "r":
        return "q"
    if text == "s":
        return "r"
    if text == "t":
        return "s"
    if text == "u":
        return "t"
    if text == "v":
        return "u"
    if text == "w":
        return "v"
    if text == "x":
        return "w"
    if text == "y":
        return "x"
    if text == "z":
        return "y"

#Uppercase letters

    if text == "A":
        return "Z"
    if text == "B":
        return "A"
    if text == "C":
        return "B"
    if text == "D":
        return "C"
    if text == "E":
        return "D"
    if text == "F":
        return "E"
    if text == "G":
        return "F"
    if text == "H":
        return "G"
    if text == "I":
        return "H"
    if text == "J":
        return "I"
    if text == "K":
        return "J"
    if text == "L":
        return "K"
    if text == "M":
        return "L"
    if text == "N":
        return "M"
    if text == "O":
        return "N"
    if text == "P":
        return "O"
    if text == "Q":
        return "P"
    if text == "R":
        return "Q"
    if text == "S":
        return "R"
    if text == "T":
        return "S"
    if text == "U":
        return "T"
    if text == "V":
        return "U"
    if text == "W":
        return "V"
    if text == "X":
        return "W"
    if text == "Y":
        return "X"
    if text == "Z":
        return "Y"

#Common punctuation marks

    if text == "=":
        return " "
    if text == "+":
        return "-"
    if text == ">":
        return "."
    if text == "<":
        return "?"
    if text == ":":
        return ","
    if text == "“":
        return "!"

#Numbers

    if text == "1":
        return "0"
    if text == "2":
        return "1"
    if text == "3":
        return "2"
    if text == "4":
        return "3"
    if text == "5":
        return "4"
    if text == "6":
        return "5"
    if text == "7":
        return "6"
    if text == "8":
        return "7"
    if text == "9":
        return "8"
    if text == "0":
        return "9"


def get_code(text):
    list_to_code = break_text(text)      # Takes a text and uses the break_text function to create a list with letters.
    coded_text = ""
    for x in list_to_code:               # Goes over te list and changes each index
        coded_text += str(code_text(x))
    return coded_text


def get_decode(text):                         # Takes a text and uses the break_text function to create a list with letters.
    list_to_decode = break_text(text)
    decoded_text = ""
    for x in list_to_decode:            # Goes over te list and changes each index
        decoded_text += str(decode_text(x))
    return decoded_text