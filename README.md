# music_retrieve
A music retrieve demo in Python

### 0. Setup Environment
This project is running in Python3.x, and please enusre following packages are installed:
- librosa
- pyaudio
- wave
- numpy
- dtw

### 1. How to run
(1) Put the music library in folder `music_base`, during which the algorithm will recognize the playing music and output a similiar music, the supported format is `.wav`.

(2) Run script `librosa_music.py`, a music retrieve database is created and stored as `beatDatabase.npy`.

(3) Make sure the microphone on your computer works fine. Run script `librosa_main.py`, and in the meanwhile play a song on your smart phone, the mactched song can be recognized in 20 seconds.

### 2. Underlying principle
```
Music signals in library->beat time extraction->beat feature->beat database
                                                                    |
                                                                    |
Music signals in the air->beat time extraction->beat feature->sequence match using dtw
->output the song with minimum distance
```

### 3. Reference
[http://librosa.github.io/librosa/generated/librosa.beat.beat_track.html#librosa.beat.beat_track](http://librosa.github.io/librosa/generated/librosa.beat.beat_track.html#librosa.beat.beat_track)
[https://labrosa.ee.columbia.edu/projects/beattrack/](https://labrosa.ee.columbia.edu/projects/beattrack/)

### 4. Blog for this project
[用Python实现一个简易的“听歌识曲”demo（一）](https://blog.csdn.net/wblgers1234/article/details/82499161)