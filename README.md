## Project: Transformer

The fundamental purpose of this project is creating a python library that enables to open various data file formats and even to transform
the data file into different file formats.





## Dependencies

You can open and save WAV files with pure python. For opening and saving non-wav 
files – like mp3 – you'll need [ffmpeg](http://www.ffmpeg.org/) or 
[libav](http://libav.org/).

### Installation

Installing pydub is easy, but don't forget to install ffmpeg/avlib (the next section in this doc)

    pip install pydub

Or install the latest dev version from github (or replace `@master` with a [release version like `@v0.12.0`](https://github.com/jiaaro/pydub/releases))…

    pip install git+https://github.com/jiaaro/pydub.git@master

-OR-

    git clone https://github.com/jiaaro/pydub.git

-OR-

Copy the pydub directory into your python path. Zip 
[here](https://github.com/jiaaro/pydub/zipball/master)

### Playback

You can play audio if you have one of these installed (simpleaudio _strongly_ recommended, even if you are installing ffmpeg/libav):

 - [simpleaudio](https://simpleaudio.readthedocs.io/en/latest/)
 - [pyaudio](https://people.csail.mit.edu/hubert/pyaudio/docs/#)
 - ffplay (usually bundled with ffmpeg, see the next section)
 - avplay (usually bundled with libav, see the next section)
 
```python
from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_file("mysound.wav", format="wav")
play(sound)
```

## Quick Start _Audio

load_audio

    song=audio.load_audio("iu.mp3",30,40)

save_audio

    audio.save_audio("sample6.mp3","sample7.wav") 

