from autorepitch import autorepitch


# executes autorepitch() using text-input in the... command line? console?
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
