import os

import librosa as lbr

from Audiolab.noteid import get_valid_name, get_valid_num


# saves a pitch-shifted version of a sample for each note in the range given by lims
def autorepitch(filepath, root, lims, short_name):
    # ensures 'note' arguments (root & lims) become valid integer representations
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
    print('Pitch-shift from ' +
          get_valid_name(min(lims))+'('+str((min(lims)))+')'+' to ' +
          get_valid_name(max(lims))+'('+str((max(lims)))+')' +
          ' stored in '+filepath)
    return None


# creates and returns a new directory for the repitch files
def new_repitch_directory(filepath):
    head, tail = os.path.split(filepath)
    tail = tail.split('.')[0]+' Samples'
    filepath = os.path.join(head, tail)
    try:
        os.mkdir(filepath)    # make the new directory
    except FileExistsError:
        pass
    return filepath


# generates a filepath with note number, name & custom short_name to save pitch-shifted sample under
def get_repitched_name(filepath, current, short_name):
    label = str(current)+'_'+get_valid_name(current)+'_'+short_name+'.wav'
    full_name = os.path.join(filepath, label)
    return full_name


# executes autorepitch() using user input prompts
def run():
    filename = input('Enter filepath: ')
    root = input('Enter root note of sample: ')
    lim1 = input('Enter the first limit of your desired pitch-shift range: ')
    lim2 = input('Enter the second limit of your desired pitch-shift range: ')
    short_name = input('Enter a short name for the pitch-shifted samples to be saved under: ')
    autorepitch(filename, root, [lim1, lim2], short_name)
    return None


if __name__ == '__main__':
    run()


