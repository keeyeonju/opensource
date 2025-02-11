# Project: Transformer

The fundamental purpose of this project is creating a python library that enables to open various data file formats and even to transform the data file into different file formats.


## Dependencies_Image
Image library enables you to simply open, edit and save image files in various formats. No matter what format you want to open or save in, you can just import the library and try it!
Before you start, there are few libraries that you have to install:

-PIL (https://pypi.org/project/Pillow/)
 
    pip install PIL

-matplotlib (https://pypi.org/project/matplotlib/)
 
    pip install matplotlib
   
## Dependencies_Data
You can open files in multiple formats with this single data library and convert them to the format of your choice.
It also has the ability to save the analyzed and used dataframes to a file of the desired format. You can create a new txt file in Python, or add content to an existing txt file.

Available format : 
  
    csv, json, xml, pdf, html, txt

installation before use : 
   
    pip install tabula-py
   
    pip install PyPDF2
   
    pip install pdfkit
    
    xml.etree.ElementTree

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
 

## Dependencies_Video
 You can open files in multiple formats with this single video library and convert them to the format of your choice. It also has the ability to save the analyzed and used dataframes to a file of the desired format.

Available format :
      ```avi, mp4, flv, bmp, ```

### Installation
#video

1.install code
```
python -m pip install opencv-python

check code
import cv2
print(cv2.__version__)

result : 4.1.0
```
2.install code
```
pip3 install moviepy
  
  pip3 install moviepy
Pip version 19.2.3 is used, but version 19.3.1 is required
```
#youtube
```
pip install pafy 
pip install youtube-dl
```

## Quick Start _Image
There are basically two parts in Image library: Image and Image_save. Image is for opening and editing an Image file and Image_save is for saving an image file in different format.
```
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

## Quick Start _Data
```python
#import module
from transformer import data

#file open (except xml)
data_file=data.open_data("mydata")

#xml_file
data_file=data.open_data("mydata","node1","node2")

#trans
data.trans("mydata",'form')

#trans_Dataframe
data.trans_dataframe(mydataframe,'form','file_name')

#pdfSlice

# 1)page 1 to 3
data.pdfSlice("myfile.pdf",1,3)

# 2)only page 5
data.pdfSlice("myfile.pdf",5)

#write_txt

# 1)create new txt file
text="text that you want to save"
data.write_txt('file_name',text,'w')  #'w' mode

# 2)Append text to an existing file
text="text that you want to add"
data.write_txt('file_name',text,'a') #'a' mode
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
## Quick Start _video
load_video
```python
#영상 재생
address='C:/Users/jinee/gitt/opensource/test.mp4'
trial=video(address)
trial.videoOpen()
save_video
#영상 캡쳐
trial.videoCapture().
#영상 변환 저장 및 자르기
trial.videoCut("avi")
 ```
save_video
```python
#영상 변환 저장 및 자르기
trial.videoCut("avi")
#유튜브 저장
url=
trial_2=Youtube(url)
trial_2.download()
