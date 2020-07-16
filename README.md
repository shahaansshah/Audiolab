# Audiolab
A space for the development of audio-related tools.

## Next Steps
- Seaborn
- open a github issue for only mono support (based on the fact
that librosa only supports mono)
- Consult whether my project structure & import methods are solid
    - Should the autorepitch (& similar) function need it's own package,
    if it's gonna have a run & perhaps some type of tests file?
    - I could put it in a package called `tools` and then put its run code in the
    `if __name__='__main__'` condition, containing it all to 1 module

---

#### Other Tasks
- `autorepitch` should be able to take filepaths or arrays
- So... unit tests, huh. Say the *autorepitch* folder (soon to be package)
is just `autorepitch.py` & `run.py`...   I'd think there should
also be a `unit_test.py` & so on.