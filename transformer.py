#!/usr/bin/env python
# coding: utf-8



from pydub import AudioSegment
from pydub.playback import play


##audio class##

class audio:
    def load_audio(name="",start_sec=0,end_sec=0):
        if name[-3:]=="wav":
            sound = AudioSegment.from_file(name, format="wav")
            if (start_sec!=0):
                a=1000*start_sec
                play(sound[a:])
            
            elif(end_sec==0):
                play(sound)
                
            else:
                a=1000*start_sec
                b=1000*end_sec
                play(sound[a:b])
            
            return sound
        if name[-3:]=="mp3":
            sound = AudioSegment.from_file(name, format="mp3")
            play(sound)
            return sound

        
        
    def save_audio(name,change_name):
        sound = AudioSegment.from_file(name, format=name[-3:])
        sound.export(change_name, format=change_name[-3:])

        
#song=audio.load_audio("sample.wav",0,3)
#audio.save_audio("sample.wav","sample6.mp3")
#last_5_seconds = song[-1000:]
#play(last_5_seconds)









