# executes autorepitch() using text-input in the... command line? console?

from Audiolab.autorepitch.auto_repitch import autorepitch


def run():
    filename = 'C:\\Users\shaha\Music\Projects & Resources\E6sine.wav'
    root, lim1, lim2 = 88, 90, 90
    short_name = 'e6short'
    # filename = input('Enter filepath: ')
    # root = input('Enter root note of sample: ')
    # lim1 = input('Enter the first limit of your desired pitch-shift range: ')
    # lim2 = input('Enter the second limit of your desired pitch-shift range: ')
    # short_name = input('Enter a short name for the pitch-shifted samples to be saved under: ')
    autorepitch(filename, root, [lim1, lim2], short_name)
    return None


if __name__ == '__main__':
    run()

# Okay, so currently the autorepitch package is being imported
# and so the only thing accessible in this file is autorepitch()
# (due to __init__.py)... but what I want to do is to, rather than
# importing the package, reference the module itself somehow (since
# we're in the same directory) and access its functions in that manner
# (that way, this script will work so long as run.py & auto_repitch.py
# are in the same directory.
#
#
# Suppose I rename the module to auto_repitch.py... these following WORK:
#
# - from autorepitch.autorepitchf import autorepitch
#   --> this explicit import allows me to pull any function in the module,
#       not be restricted by the package restrictions
#   --> but there's some namespace issues if I call the module
#       what the package is called
#
# - from autorepitchf import autorepitch
#   --> this works the way I want it too (I get access to other functions
#       written in the module), but it's red-underlined by Pycharm
#   --> this also still fully works if the module is called auto_repitch.py
#       (Like, get_repitched_name also fully works) - still red-underlined
#   --> This is probably because python now wants us to explicitly specify
#       relative and absolute import commands...
#
#
# So, I guess the question is, how do I deal with namespace issues if I want
# to call a module the same thing as the package it's in? I thought it would
# be what's shown below, but there's a namespace issue! Relative namespace
# doesn't work either.
#
# - from autorepitch.autorepitch import autorepitch
#   --> 'ModuleNotFoundError: No module named 'autorepitch.autorepitch'; 'autorepitch' is not a package'
#   --> autorepitch.autorepitchf.__name__ == autorepitch.autorepitchf
#   --> autorepitch.autorepitch.__name__ == autorepitch
#
# - from .autorepitch import autorepitch
#   --> ImportError: attempted relative import with no known parent package
#
# - from .autorepitchf import autorepitch
#   --> ImportError: attempted relative import with no known parent package
#
#   --> The two above would be due to the fact that if you're running main directly,
#       __name__ and __path__ (& what else?) wouldn't be set to the current package,
#       so it doesn't know where '.' is. So for the purposes of run.py, relative
#       imports don't cut it.
