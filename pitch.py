# This module parses, standardises and converts pitch values, independent of the Note class.
# - names:   <letter>[<accidental>]<octave>, eg. "F#5". Any integer octave is allowed (no MIDI range limit on names).
# - numbers: MIDI note numbers, which must lie in MIDI_TUNING_RANGE.
# Every function validates its input and raises a PitchError subclass (see exceptions.py) on failure,
# so anything it returns is already in canonical form.

import re
from typing import Tuple, Union
from config import MIDI_TUNING_RANGE, NOTE_NAMES_VALUES, ACCIDENTALS_VALUES, C1_OFFSET
import exceptions as exc


_LETTERS = "|".join(re.escape(n) for n in NOTE_NAMES_VALUES)
_ACCIDENTALS = "|".join(re.escape(a) for a in ACCIDENTALS_VALUES)

# compiled once at import; case-insensitive, optional whitespace before the octave, eg. "f#  5", "bb3", "C-1"
NAME_PATTERN = re.compile(
    rf"(?P<letter>{_LETTERS})(?P<accidental>{_ACCIDENTALS})?\s*(?P<octave>-?\d+)",
    re.IGNORECASE,
)
_CANONICAL_ACCIDENTALS = {a.lower(): a for a in ACCIDENTALS_VALUES}


# --- names ---

def parse_name(name: str) -> Tuple[str, str, int]:
    """Split a note name into canonical (letter, accidental, octave), eg. "bb3" -> ("B", "b", 3).
    The accidental is "" for naturals. Raises InvalidNoteName if the string is malformed."""
    match = NAME_PATTERN.fullmatch(name)
    if not match:
        raise exc.InvalidNoteName(name)
    accidental = _CANONICAL_ACCIDENTALS[match["accidental"].lower()] if match["accidental"] else ""
    return match["letter"].upper(), accidental, int(match["octave"])


def format_name(letter: str, accidental: str, octave: int) -> str:
    """Join canonical name parts into a name string."""
    return f"{letter}{accidental}{octave}"


def normalise_name(name: str) -> str:
    """Return the canonical form of a note name, eg. "f#  5" -> "F#5"."""
    return format_name(*parse_name(name))


# --- numbers ---

def parse_num(value: Union[int, str]) -> int:
    """Return value as an int MIDI note number. Accepts an int or a decimal string.
    Raises InvalidMIDINumber if it is not a number or lies outside the MIDI tuning range."""
    try:
        num = int(value)
    except (ValueError, TypeError):
        raise exc.InvalidMIDINumber(value, MIDI_TUNING_RANGE) from None
    if num not in MIDI_TUNING_RANGE:
        raise exc.InvalidMIDINumber(num, MIDI_TUNING_RANGE)
    return num


# --- conversions ---

def num_from_name(name: str) -> int:
    """Convert a note name to its MIDI number, eg. "C4" -> 60.
    Raises InvalidNoteName if malformed, InvalidMIDINumber if the name is valid but outside the MIDI range (eg. "C0")."""
    letter, accidental, octave = parse_name(name)
    pitch_class = NOTE_NAMES_VALUES[letter] + (ACCIDENTALS_VALUES[accidental] if accidental else 0)
    return parse_num(C1_OFFSET + 12 * (octave - 1) + pitch_class)


def name_from_num(num: Union[int, str]) -> str:
    """Convert a MIDI number to its canonical name (sharps for black keys), eg. 61 -> "C#4".
    Raises InvalidMIDINumber if outside the MIDI range."""
    offset = parse_num(num) - C1_OFFSET
    octave, pitch_class = offset // 12 + 1, offset % 12
    for letter, value in NOTE_NAMES_VALUES.items():
        if value == pitch_class:
            return format_name(letter, "", octave)
        if value + ACCIDENTALS_VALUES["#"] == pitch_class:
            return format_name(letter, "#", octave)
    raise RuntimeError(f"NOTE_NAMES_VALUES in config.py cannot express pitch class {pitch_class}")
