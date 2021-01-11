import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import librosa as lbr


load_path = 'C:\\Users\shaha\Music\Projects & Resources\E6sineshort.wav'
wave, sr = lbr.load(load_path, sr=None)
t = np.arange(0, len(wave)/sr, 1/sr)
new_wave = lbr.effects.pitch_shift(wave, sr=sr, n_steps=0)

sns.set()

# Load an example dataset with long-form data
data = wave

# Plot the responses for different events and regions
sns.lineplot(data=wave)
plt.show()

# Next steps:
# - Seaborn
# - Do an analysis of similar in the time-domain signals
# - Do an analysis of similar in the frequency domain signals
