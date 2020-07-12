
# In this file is a class called 'Note', meant to associate a letter note name (eg. C#7) with a number (97).
# Currently, the construction of a note is allowed in the MIDI tuning range: from A0 (21) to G#9 (128)

# NEXT STEPS:
# - should a note be a class or a data type? It is just meant to provide
#   an analog between number labels and name labels.
#
# - deleting whatever git repo I've created, and starting a new one in a folder within Audiolab,
#   where these project files should live...
#   --> my current idea right now is to have every tool/project in the Audiolab venv, but set up
#       individual git repositories for different projects.
#
# - questions about dependencies and structure organization (keeping Note class/data structure independent)


validRange = range(21, 129)  # specifies the MIDI tuning range
names = [   # assigns numbers to names to allow equation between names & numbers
    ['B', 11],
    ['A', 9],
    ['G', 7],
    ['F', 5],
    ['E', 4],
    ['D', 2],
    ['C', 0],
    ['#', 1],
    ['b', -1]
]


class Note:
    name = None
    num = None

    def __init__(self, val):  # populates vars if given an int in validRange, or a valid string note name (eg. C#7)
        # checking for int in validRange, & populating if so
        if type(val) == int:
            self.num = self.checkNumValidity(val)
            self.name = self.numToName(val)
        # or checking for valid string, & populating if so
        elif type(val) == str:
            self.name = self.checkStringValidity(val)
            self.num = self.nameToNum(self.name)
        else:
            raise SyntaxError("Invalid note constructor argument. Must be either "
                              "an integer within MIDI tuning range (21 to 128) or "
                              "a string with note name & octave (eg. Bb2, G#7) from A0 to G#9")

    def checkNumValidity(self, num):    # checks whether valid number was passed to create note object
        n = num
        if n not in validRange:
            raise SyntaxError("Invalid integer value. Must be within MIDI tuning range (21 to 128).")
        return n

    def checkStringValidity(self, string):  # checks whether valid string was passed to create note object
        s = list(string)
        s[0] = s[0].upper()
        if s[0] not in ['C', 'D', 'E', 'F', 'G', 'A', 'B']:    # checking if first char is a white note
            raise SyntaxError("Invalid note name. First character must be a white note.")
        i = 1
        if s[i] in ['#', 'b']:   # checking if 2nd char is accidental
            i += 1
        alldigits = "".join(s[i:]).isdigit()
        if not alldigits:   # checking if all remaining chars are digits
            raise SyntaxError("Invalid octave number. Must be an integer from 0 to 9.")
        newstring = "".join(s)
        if self.nameToNum(newstring) not in validRange:    # checking if that number is in validRange
            raise SyntaxError("Invalid octave range. Must be from A0 to G#9.")
        return newstring

    def nameToNum(self, name):
        i = 0
        while name[i-1].isdigit():
            i -= 1
        name, octv = name[:i], int(name[i:])    # splits name into its (letter/accidental) & (octave)
        num = 12*(octv+1)
        for char in name:
            for pair in names:
                if char == pair[0]:
                    num += pair[1]
                    break
        return num

    def numToName(self, num):
        name, accid = None, None
        num -= 12
        octv = num//12
        num -= octv*12
        for pair in names:
            if pair[1] <= num:
                name = pair[0]
                num -= pair[1]
                break
        if num == 1:
            accid = '#'
            num -= 1
        if num == 0:
            name = name+(accid or '')+str(octv)
        return name

    def incNoteVal(self, inc):  # increments the value of the note object
        if type(inc) != int:
            raise SyntaxError("Argument must be an integer.")
        if self.num+inc not in validRange:
            raise SyntaxError("New note value not in valid MIDI tuning range.")
        self.num += inc
        self.name = self.numToName(self.num)
        return None

    def changeNoteVal(self, newnote):   # changes the value of the note object
        if type(newnote) == int:
            self.num = self.checkNumValidity(newnote)
            self.name = self.numToName(newnote)
        # or checking for valid string, & populating if so
        elif type(newnote) == str:
            self.name = self.checkStringValidity(newnote)
            self.num = self.nameToNum(self.name)
        else:
            raise SyntaxError("Invalid note change argument. Must be either "
                              "an integer within MIDI tuning range (21 to 128) or "
                              "a string with note name & octave (eg. Bb2, G#7) from A0 to G#9")
        return None
