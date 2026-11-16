class AudiolabError(Exception):
    """Root of all errors raised deliberately by this project. Catch this to handle any of them."""


class PitchError(AudiolabError, ValueError):
    """A pitch value (name, number, ...) was the right type but cannot be interpreted or represented.
    Stores the offending value. Raised by pitch.py and anything built on it, not just by Note."""

    def __init__(self, value, message: str):
        super().__init__(f"{message} (got {value!r})")
        self.value = value


class InvalidNoteName(PitchError):
    """A string is not of the form <letter>[<accidental>]<octave>. Says nothing about MIDI range."""

    def __init__(self, value):
        super().__init__(
            value,
            "Invalid note name. Must be a valid note letter (with optional '#' or 'b'), followed by an octave number",
        )


class InvalidMIDINumber(PitchError):
    """A number is outside the MIDI tuning range, whether given directly or derived from a name."""

    def __init__(self, value, valid_range: range):
        super().__init__(
            value,
            f"Invalid MIDI note number. Must be in MIDI tuning range ({min(valid_range)}-{max(valid_range)})",
        )
        self.valid_range = valid_range


class InvalidNoteInput(AudiolabError, TypeError):
    """A Note was constructed from something that is neither an int nor a str."""

    def __init__(self, value):
        super().__init__(
            f"Invalid note input. Must be a valid string name or integer number (got {type(value).__name__}: {value!r})"
        )
        self.value = value
