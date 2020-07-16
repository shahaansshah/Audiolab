import librosa as lbr

# import autorepitch as arp
load_path = 'C:\\Users\shaha\Music\Projects & Resources\E6sineshort.wav'
# head, tail = os.path.split(load_path)
# new_path = os.path.join(head,tail.split('.')[0]+'_processed.wav')
# lbr.output.write_wav(new_path, new_wave, sr=sr, norm=False)

wave, sr = lbr.load(load_path, sr=None)
new_wave = lbr.effects.pitch_shift(wave, sr=sr, n_steps=0)

# t = np.arange(0, len(wave)/sr, 1/sr)
# plt.plot(t,wave,t,new_wave)
# plt.show()
# plt.plot(t,wave-new_wave)
# plt.show()



# Next steps:
# - Seaborn
# - Do an analysis of similar in the time-domain signals
# - Do an analysis of similar in the frequency domain signals