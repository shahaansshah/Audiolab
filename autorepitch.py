import os
import librosa as lbr

from noteid import get_valid_name, get_valid_num


def autorepitch(filepath, root, lims, short_name):
    # ensures root, current and limit are all valid integers
    root = get_valid_num(root)
    lims = [get_valid_num(lims[0]), get_valid_num(lims[1])]
    current, limit = min(lims), max(lims)

    wave, sr = lbr.load(filepath, sr=None)  # load audio file
    filepath = new_repitch_directory(filepath)  # create new directory for samples

    # pitch-shift & save sample for every note in the given range
    while current <= limit:
        new_wave = lbr.effects.pitch_shift(wave, sr=sr, n_steps=current-root)
        new_name = get_repitched_name(filepath, current, short_name)
        lbr.output.write_wav(new_name, new_wave, sr=sr, norm=False)
        current += 1

    # print mission success!
    print('Pitch-shift from '+
          get_valid_name(min(lims))+'('+str((min(lims)))+')'+' to ' +
          get_valid_name(max(lims))+'('+str((max(lims)))+')' +
          ' stored in '+filepath+'.')
    return None


def new_repitch_directory(filepath):    # creates and returns a new directory for the repitch files
    head, tail = os.path.split(filepath)
    tail = tail.split('.')[0]+' Samples'
    filepath = os.path.join(head, tail)
    try:
        os.mkdir(filepath)    # make the new directory
    except FileExistsError:
        pass
    return filepath


def get_repitched_name(filepath, current, short_name):
    label = str(current)+'_'+get_valid_name(current)+'_'+short_name+'.wav'
    full_name = os.path.join(filepath, label)
    return full_name


def run():  # the UI component
    filename = input('Enter filepath: ')
    root = input('Enter root note of sample: ')
    lim1 = input('Enter the first limit of your desired pitch-shift range: ')
    lim2 = input('Enter the second limit of your desired pitch-shift range: ')
    short_name = input('Enter a short name for the pitch-shifted samples to be saved under: ')
    autorepitch(filename, root, [lim1, lim2], short_name)
    return None


# C:\Users\shaha\Music\Projects & Resources\C U Girl - Steve Lacy\C U Girl Short Loop.wav
run()

# *****NEXT STEPS*****
# - I think it makes sense for noteid.py to be where it is,
#   not restricted in the autorepitch directory. How do I
#   deal with this in regards to the repository?
#
# - What should the autorepitch folder structure be? I'm thinking
#   a package, with a... main/run esque file... inside it? Outside it?
#   Is run() good where it is, in this file?
#
# - Should I even make it a package? There's just 1 function I want
#   to be accessible from this directory.
#
# - What's the proper way I should be organizing the dependencies
#   between these modules? Relevant if I make a separate main()/run()
