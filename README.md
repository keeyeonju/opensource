# Project: Transformer

The fundamental purpose of this project is creating a python library that enables to open various data file formats and even to transform the data file into different file formats.


## Dependencies_Image
Image library enables you to simply open, edit and save image files in various formats. No matter what format you want to open or save in, you can just import the library and try it!
Before you start, there are few libraries that you have to install:

-PIL (https://pypi.org/project/Pillow/)

-matplotlib (https://pypi.org/project/matplotlib/)


## Dependencies_Audio

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

## Quick Start _Image
There are basically two parts in Image library: Image and Image_save. Image is for opening and editing an Image file and Image_save is for saving an image file in different format.

-Image
```python
trial=Image(address) >> Execute the Image class with the variable "address"
#Open an Image file
data=trial.openImage() >>The imported image file is saved in 'data'

#Open an Image file in X, Y-axis
trial.imageArray()

#Resize the image file
trial.resizeImage(x, y)

#Rotate the image file
trial.rotateImage(degree)

#Flip the image file
trial.flipImage(direction) >>direction should be either "hoz" or "ver"

#Crop the image file
trial.cropImage(x1, y1, x2, y2)

-Image_save
```python
trial=Image_save(address) >> Execute the Image_save class with the variable "address"
#Save the image file in different format
trial.save_ ("Title")>>insert the format you want to save the image file in after 'save_'
```


## Quick Start _Audio

load_audio
```python
#전체 재생
song=audio.load_audio("iu.mp3")
#30초부터 전체 재생
song=audio.load_audio("iu.mp3",30)
#30초부터 40초까지 재생
song=audio.load_audio("iu.mp3",30,40)
 ```
save_audio
    
```python
#"sample.mp3"를 "sample7.wav"로 변환
audio.save_audio("sample6.mp3","sample7.wav") 
```

