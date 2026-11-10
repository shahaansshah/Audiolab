

from config import MIDI_TUNING_RANGE


invalid_Note_input = TypeError("Invalid note input. Must be a valid string name or integer number.")
invalid_Note_number = ValueError("Invalid note number. Must be in MIDI tuning range ({}-{})".format(min(MIDI_TUNING_RANGE), max(MIDI_TUNING_RANGE)))
invalid_Note_name = ValueError("Invalid note name. Must be a valid note letter (with optional '#' or 'b'), followed by octave number")
