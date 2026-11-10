# *****WHAT IS THIS???*****
# This module defines the fundamental note object, which is used to represent a musical note in the program. It entails:
# - a valid name, made of the Western note names and accidentals [C D E F G A B # b] and an octave number (eg. c4, f#5, g#3)
# - a note number representinng the note's position in the MIDI tuning range 21 (A0) to 128 (G#9)
# - only notes in the MIDI tuning range are valid, and only notes that can be constructed out of the characters in the 'names' array below are valid
#   (no half or double accidentals, etc.)

import re
from typing import Union
from config import MIDI_TUNING_RANGE, NOTE_NAMES_VALUES, ACCIDENTALS_VALUES, MIDI_VALID_OCTAVES
import exceptions as exc


class Note:
    
    def __init__(self, value: Union[int, str]):

        self.name = None
        self.num = None
        
        # if integer was passed (as type int or str), check it is in valid MIDI tuning range, assign to self.num
        if(
            type(value) == int or
            type(value) == str and value.isdecimal()
        ):
            value = int(value)
            if value in MIDI_TUNING_RANGE:
                self.num = value
            else:
                raise exc.invalid_Note_number
            
        # if non-integer string was passed, check for valid note name, assign to self.name
        elif type(value) == str:

            # 
            letters = "|".join(re.escape(n) for n in NOTE_NAMES_VALUES)
            accidentals = "|".join(re.escape(a) for a in ACCIDENTALS_VALUES)
            octaves = "|".join(str(o) for o in sorted(MIDI_VALID_OCTAVES, reverse=True))

            # 
            valid_name = re.compile(
                rf"(?P<letter>{letters})(?P<accidental>{accidentals})?\s*(?P<octave>{octaves})",
                re.IGNORECASE,
            )

            # if input value matches the valid_name pattern, normalise to canonical form and assign to self.name
            match = valid_name.fullmatch(value)
            if match:

                # normalise to canonical form, eg. "f#  5" style input -> "F#5", "bb3" -> "Bb3"
                accidental_keys = {a.lower(): a for a in ACCIDENTALS_VALUES}
                accidental = accidental_keys[match["accidental"].lower()] if match["accidental"] else ""

                # assign to self.name
                self.name = f"{match['letter'].upper()}{accidental}{match['octave']}"
            
            else:
                raise exc.invalid_Note_name

        # if neither int nor str was passed, raise TypeError
        else:
            raise exc.invalid_Note_input

        try:
            print(self.name)
        except Exception:
            print(self.num)
