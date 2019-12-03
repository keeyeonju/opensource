#!/usr/bin/env python
# coding: utf-8



from pydub import AudioSegment
from pydub.playback import play
from PyPDF2 import PdfFileReader, PdfFileWriter


##Audio class##

class audio:
    def load_audio(name="",start_sec=0,end_sec=0):
        if name[-3:]=="wav":
            sound = AudioSegment.from_file(name, format="wav")
            if(start_sec==0 & end_sec==0):
                play(sound)
                
            elif (end_sec==0):
                a=1000*start_sec
                play(sound[a:])            
                
                
            else:
                a=1000*start_sec
                b=1000*end_sec
                play(sound[a:b])
            
            return sound
        
        
        if name[-3:]=="mp3":
            sound = AudioSegment.from_file(name, format="mp3")
            if(start_sec==0 & end_sec==0):
                play(sound)
                
            elif (end_sec==0):
                a=1000*start_sec
                play(sound[a:])
       
                
            else:
                a=1000*start_sec
                b=1000*end_sec
                play(sound[a:b])
            
            return sound

    
        
    def save_audio(name,change_name):
        sound = AudioSegment.from_file(name, format=name[-3:])
        sound.export(change_name, format=change_name[-3:])


  