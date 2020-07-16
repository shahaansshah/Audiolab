# *****WHAT IS THIS???*****
# This module provides two functions intended for importation into other modules:
# - get_valid_num
# - get_valid_name
# that enable the conversion between or obtainment of a note name (eg. c4) & note number (60),
# within the range specified by validRange (currently set to the MIDI tuning range, from 21 (A0) to 128 (G#9)).
#
#
# *****USEFUL INFO*****
# - This module only works for notes that can be constructed out of the characters in the 'names' array below -
#   no half or double accidentals, or other crazy business.
# - The Western music note names & accidentals, [C D E F G A B # b],
#   are hardcoded in check_valid_name (as well as '#' in num_to_name)
# - When using num_to_name, black notes are always named with sharps.


validRange = range(21, 129)

names = [
    ['B', 11],
    ['A', 9],
    ['G', 7],
    ['F', 5],
    ['E', 4],
    ['D', 2],
    ['C', 0],
    ['#', 1],
    ['b', -1]
]


def get_valid_num(note):
    if type(note) == str:
        note = name_to_num(note)
    elif type(note) == int:
        note = check_valid_num(note)
    else:
        raise TypeError('Invalid note. Must be a string name or int number.')
    return note


def get_valid_name(note):
    if type(note) == str:
        note = check_valid_name(note)
    elif type(note) == int:
        note = num_to_name(note)
    else:
        raise TypeError('Invalid note. Must be a string name or int number.')
    return note


def name_to_num(name: str):
    name = check_valid_name(name)   # checks if name is formatted correctly
    num = valid_name_to_num(name)   # assuming a correctly-formatted name, gets the number (if it's in validRange)
    return num


def num_to_name(num: int):  # Black notes are always named with sharps
    num = check_valid_num(num)-12
    octv = num // 12
    num -= octv * 12
    name, accid = None, None
    for pair in names:
        if pair[1] <= num:
            name = pair[0]
            num -= pair[1]
            break
    if num == 1:
        accid = '#'
        num -= 1
    name = name + (accid or '') + str(octv)
    return name


def check_valid_num(num: int):
    if type(num) != int:
        raise TypeError('Must pass an integer into this function.')
    if num not in validRange:
        raise ValueError('Note number out of validRange. Must be from ' +
                         str(min(validRange)) + ' to ' +
                         str(max(validRange)) + '.')
    return num


def check_valid_name(name: str):
    if type(name) != str:
        raise TypeError('Must pass a string into this function.')
    i = 1
    s = list(name)
    s[0] = s[0].upper()
    if s[0] not in ['C', 'D', 'E', 'F', 'G', 'A', 'B']:  # checking if first char is a white note
        raise ValueError("Invalid note name. First character must be a white note.")
    if s[i] in ['#', 'b']:  # checking if 2nd char is accidental
        i += 1
    letters = "".join(s[:i])
    digits = "".join(s[i:])
    aredigits = digits.isdigit()
    if not aredigits:  # checking if all remaining chars are digits
        raise ValueError('Invalid entry. Note must be from ' +
                         str(num_to_name(min(validRange))) + ' to ' +
                         str(num_to_name(max(validRange))) + '.')
    # At this point, we know if the string is in the right format:
    # Now we just check if the note is in validRange
    name = "".join([letters, digits])
    valid_name_to_num(name)
    return name


def valid_name_to_num(name: str):
    i = 0
    temp_name = name
    while temp_name[i-1].isdigit():
        i -= 1
    temp_name, octave = temp_name[:i], int(temp_name[i:])    # splits temp_name into its (letter/accidental) & (octave)
    num = 12*(octave+1)
    for char in temp_name:
        for pair in names:
            if char == pair[0]:
                num += pair[1]
                break
    if num not in validRange:
        raise ValueError('Note out of validRange. Note must be from ' +
                         str(num_to_name(min(validRange))) + ' to ' +
                         str(num_to_name(max(validRange))) + '.')
    return num
