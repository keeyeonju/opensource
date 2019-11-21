#!/usr/bin/env python
# coding: utf-8



from pydub import AudioSegment
from pydub.playback import play


##audio class##

class audio:
    def load_audio(name):
        if name[-3:]=="wav":
            sound = AudioSegment.from_file(name, format="wav")
            play(sound)
            return sound
        if name[-3:]=="mp3":
            sound = AudioSegment.from_file(name, format="mp3")
            play(sound)
            return sound

        
        
    def save_audio(name,change_name):
        sound = AudioSegment.from_file(name, format=name[-3:])
        sound.export(change_name, format=change_name[-3:])
        
#song=audio.load_audio("sample.wav")
#audio.save_audio("sample.wav","sample6.mp3")









