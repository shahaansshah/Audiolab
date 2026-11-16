MIDI_TUNING_RANGE = range(21, 129)
NOTE_NAMES_VALUES = {
    "C": 0,
    "D": 2,
    "E": 4,
    "F": 5,
    "G": 7,
    "A": 9,
    "B": 11
}
ACCIDENTALS_VALUES = {
    "#": 1,
    "b": -1
}
# Floor of MIDI_TUNING_RANGE is (defined?) as A0
A0_OFFSET = min(MIDI_TUNING_RANGE)
C1_OFFSET = A0_OFFSET + (12 - abs(NOTE_NAMES_VALUES["C"] - NOTE_NAMES_VALUES["A"]))
# VALID_OCTAVES assumes that the valid MIDI range will include the 0th octave notes, and thus will start at 0
MIDI_VALID_OCTAVES = range(1 + (max(MIDI_TUNING_RANGE) - 12) // 12)
