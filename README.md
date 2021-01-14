# Audiolab
A space for the development of audio-related tools.

## autorepitch
Generates pitch-shifted audio samples of a given audio
file, within a range of notes specified by the user.
It was developed to aid in the process of creating soundfont files
from an audio sample. Can be used with the GUI or by calling the
function in the shell.

Here is a demonstration of the GUI being used to help create a
soundfont:   
![](autorepitch_demonstration_2.gif)

##### Next Steps
- Comments/pydocs!
- restructure `noteid.py` (an overall `get_valid_note()` function is
all that's needed)
- add more print statements so that the program is useable & can
be tracked/debugged from the console