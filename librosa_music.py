from __future__ import print_function
import librosa
import os

import numpy as np


audioList = os.listdir('music_base')
raw_audioList = {}
beat_database = {}
for tmp in audioList:
    audioName = os.path.join('music_base', tmp)
    if audioName.endswith('.wav'):
        y, sr = librosa.load(audioName)
        tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
        beat_frames = librosa.feature.delta(beat_frames)
        beat_database[audioName] = beat_frames

np.save('beatDatabase.npy', beat_database)