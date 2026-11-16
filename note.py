# *****WHAT IS THIS???*****
# This module defines the fundamental note object, which is used to represent a musical note in the program. It entails:
# - a valid name (the note's identity, always present), made of the Western note names and accidentals [C D E F G A B # b] and an octave number (eg. c4, f#5, g#3).
#   Names are not limited to the MIDI range (eg. C0 is a valid Note).
# - a note number representing the note's position in the MIDI tuning range 21 (A0) to 128 (G#9).
#   Numbers must be in that range; asking a name-built Note outside it for its number raises InvalidMIDINumber.
# All parsing and conversion lives in pitch.py; Note just holds a value and exposes it.

from typing import Optional, Union
import pitch
import exceptions as exc


class Note:

    def __init__(self, value: Union[int, str]):

        # The name is a Note's identity, so it is always set, in canonical form.
        # The MIDI number is optional: a name outside the MIDI range (eg. C0) has none.
        self._num: Optional[int] = None

        # integer (as type int or decimal str): validate as a MIDI number, derive the name from it
        if (
            type(value) == int or
            type(value) == str and value.isdecimal()
        ):
            self._num = pitch.parse_num(value)
            self._name: str = pitch.name_from_num(self._num)

        # any other string: validate as a note name; the number is derived on request
        elif type(value) == str:
            self._name = pitch.normalise_name(value)

        # neither int nor str
        else:
            raise exc.InvalidNoteInput(value)

    # A future modality (eg. frequency) adds a branch above that derives the name via a conversion in pitch.py.

    def get_name(self) -> str:
        """Return the note's canonical name, eg. 'F#5'."""
        return self._name

    def get_num(self) -> int:
        """Return the note's MIDI number. Raises InvalidMIDINumber for a valid name outside the MIDI range (eg. C0)."""
        if self._num is None:
            self._num = pitch.num_from_name(self._name)
        return self._num
