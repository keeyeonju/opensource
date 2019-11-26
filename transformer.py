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


from PyPDF2 import PdfFileReader, PdfFileWriter

def pdfSlice(file_name,first_page,last_page):

    pdf=PdfFileReader(open(file_name,'rb'))

    numberPages=pdf.getNumPages()
    
    if(last_page>numberPages):
        print("페이지 범위를 초과했습니다.")
        return 0

    for page in range(first_page,last_page):

        pdf_writer=PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        output_filename='file_name_{}.pdf'.format(page+1)

        with open (output_filename,'wb')as f:
            pdf_writer.write(f)
            
    return pdf

pdfSlice("frozen.pdf",1,3)

        






