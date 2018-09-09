# -*- coding: utf-8 -*-

from dtw import dtw
from numpy.linalg import norm
from numpy import array
import numpy as np
import librosa
import pyaudio
import wave

all_data = np.load('beatDatabase.npy')
beat_database = all_data.item()

#
# sr = 44100
# chunk = sr
# p = pyaudio.PyAudio()
# stream = p.open(format=pyaudio.paInt16,
#                 channels=1,
#                 rate=sr,
#                 input=True,
#                 frames_per_buffer=chunk)
# frames = []
# for i in range(0, int(sr / chunk * 30)):
#     data = stream.read(chunk)
#     frames.append(data)
# stream.stop_stream()
# stream.close()
# p.terminate()
# #
# wf = wave.open('music_test/test.wav', 'wb')
# wf.setnchannels(1)
# wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
# wf.setframerate(sr)
# wf.writeframes(b''.join(frames))
# wf.close()


testAudio = "music_test/test.wav"
y, sr = librosa.load(testAudio)
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
beat_frames = librosa.feature.delta(beat_frames)

x = array(beat_frames).reshape(-1, 1)

compare_result = {}
for songID in beat_database.keys():
    y = beat_database[songID]
    y = array(y).reshape(-1, 1)
    dist, cost, acc, path = dtw(x, y, dist=lambda x, y: norm(x - y, ord=1))
    print('Minimum distance found for ', songID.split("\\")[1], ": ", dist)
    compare_result[songID] = dist

matched_song = min(compare_result, key=compare_result.get)

print(matched_song)