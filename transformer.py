#!/usr/bin/env python
# coding: utf-8



from pydub import AudioSegment
from pydub.playback import play


##audio class##

class audio:
    #audio 재생 함수
    def load_audio(name):
        if name[-3:]=="wav":
            sound = AudioSegment.from_file(name, format="wav")
        if name[-3:]=="mp3":
            sound = AudioSegment.from_file(name, format="mp3")

        play(sound)

class video:
    #video 재생 함수
     def load_video(name):
         if name[-3:]=="avi":
             video = videosegment.from_file(name, format="avi")
         if name[-3:]=="wmv":
             video = videosegment.from_file(name, format="wmv")

        play(sound)






