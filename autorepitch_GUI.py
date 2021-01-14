"""Pydocs yay."""

import os
import time
import tkinter as tk
from tkinter import filedialog

from noteid import get_valid_name, get_valid_num
from auto_repitch import autorepitch


filetypes = [('wav files', '.wav')]


class GUI:
    def __init__(self, root):
        # instance variables
        self.filepath = ''
        self.filename = 'No Audio Selected'
        self.info = ''
        self.rootnote = ''
        self.lims = []
        self.newdir = ''

        # tkinter GUI elements

        # root and all-encompassing frame
        root.title('autorepitch')
        frame = tk.Frame(root, padx=5, pady=5)
        frame.pack(padx=10, pady=7)

        # 'Title' label
        label = tk.Label(frame, text='Generate pitch-shifted samples from an audio file', padx=5, pady=1)
        label.grid(row=0)

        # Select Audio button
        frame1 = tk.Frame(frame, padx=5, pady=5)
        frame1.grid(row=1)
        self.selectaudio = tk.Button(frame1, text='Select Audio', command=self.get_filepath)
        self.selectaudio.pack(side="left", padx=5, pady=5)

        # pitch entries
        pitchframe = tk.Frame(frame1, padx=5, pady=2)
        pitchframe.pack()
        rootlabel = tk.Label(pitchframe, text="Sample root pitch:")
        rootlabel.grid(row=0, column=0, sticky="e")
        self.rootentry = tk.Entry(pitchframe, width=5)
        self.rootentry.grid(row=0, column=1)
        lblabel = tk.Label(pitchframe, text="Lower bound of re-pitch range:")
        lblabel.grid(row=1, column=0, sticky="e")
        self.lbentry = tk.Entry(pitchframe, width=5)
        self.lbentry.grid(row=1, column=1)
        ublabel = tk.Label(pitchframe, text="Upper bound of re-pitch range:")
        ublabel.grid(row=2, column=0, sticky="e")
        self.ubentry = tk.Entry(pitchframe, width=5)
        self.ubentry.grid(row=2, column=1)

        # filename display
        frame2 = tk.Frame(frame, padx=5, pady=5)
        frame2.grid(row=2, sticky="w")
        self.filestr = tk.StringVar(frame2, value=self.filename)
        filelabel = tk.Label(frame2, textvariable=self.filestr, fg="grey")
        filelabel.pack()

        # info label
        frame3 = tk.Frame(frame, padx=5, pady=5)
        frame3.grid(row=3)
        self.infostr = tk.StringVar(frame3, value=self.info)
        infolabel = tk.Label(frame3, textvariable=self.infostr, wraplength=400, justify='center')
        infolabel.pack()

        # generate and view buttons
        frame4 = tk.Frame(frame)
        frame4.grid(row=4, sticky="e")
        self.generatebutton = tk.Button(frame4, text="Generate", command=self.run_autorepitch)
        self.generatebutton.grid(row=0, column=1, padx=2, pady=5)
        self.viewbutton = tk.Button(frame4, text="View Samples", state=tk.DISABLED, command=self.open_file_explorer)
        self.viewbutton.grid(row=0, column=2, padx=2, pady=5)

    def get_filepath(self):
        self.filepath = filedialog.askopenfilename(title='Select an audio sample', filetypes=filetypes)
        self.update_filename()

    def update_filename(self):
        if self.filepath != '':
            self.filename = os.path.split(self.filepath)[1]
        self.filestr.set(self.filename)

    def run_autorepitch(self):
        try:
            # processing all GUI inputs for validity
            self.filepath = self.process_filepath()
            self.rootnote = self.process_noteentry(self.rootentry, "Root pitch: ")
            lb = self.process_noteentry(self.lbentry, "Lower bound: ")
            ub = self.process_noteentry(self.ubentry, "Upper bound: ")
            self.lims = [lb, ub]
        except Exception:
            return None
        # deactivate both buttons
        self.generatebutton['state'] = tk.DISABLED
        self.viewbutton['state'] = tk.DISABLED
        # run autorepitch!
        try:
            self.info = 'Generating pitch-shifted samples...'
            self.infostr.set(self.info)
            self.viewbutton['state'] = tk.NORMAL
            self.newdir, message = autorepitch(self.filepath, self.rootnote, self.lims, '')
            self.generatebutton['state'] = tk.NORMAL

        except:
            message = 'Sorry, auto_repitch ran into a problem while generating.'
            self.generatebutton['state'] = tk.DISABLED
            self.viewbutton['state'] = tk.DISABLED
        self.info = message
        self.infostr.set(self.info)

    def process_filepath(self):
        # if filepath is blank
        if self.filepath == '':
            self.info = 'You must select an audio file.'
            self.infostr.set(self.info)
            raise Exception
        return self.filepath

    def process_noteentry(self, noteentry, string):
        entry = noteentry.get()
        if entry.isdecimal():
            entry = int(entry)
        try:
            self.info = ''
            entry = get_valid_num(entry)
            self.infostr.set(self.info)
            return entry
        except Exception as x:
            self.info = string + str(x)
            self.infostr.set(self.info)
            raise Exception

    def open_file_explorer(self):
        try:
            os.startfile(self.newdir)
        except Exception as x:
            self.info = 'Issue opening file explorer: ' + str(x)
            self.infostr.set(self.info)


if __name__ == '__main__':
    root = tk.Tk()
    window = GUI(root)
    root.mainloop()
