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



##Pdf class##

class pdf:
    def pdfSlice(file_name,first_page=0,last_page=0):

        pdf=PdfFileReader(open(file_name,'rb'))

        numberPages=pdf.getNumPages()
        if(last_page==0):
            pdf_writer=PdfFileWriter()
            pdf_writer.addPage(pdf.getPage(first_page-1))

            output_filename='{}_{}.pdf'.format(file_name[:-4],first_page)

            with open (output_filename,'wb')as f:
                pdf_writer.write(f)
            return pdf

        if(last_page>numberPages):
            print("페이지 범위를 초과했습니다.")
            return 0

        pdf_writer=PdfFileWriter()
        
        for page in range(first_page-1,last_page):

            #pdf_writer=PdfFileWriter()
            pdf_writer.addPage(pdf.getPage(page))

            #output_filename='{}_{}.pdf'.format(file_name[:-4],page+1)
        output_filename='{}_{}_{}.pdf'.format(file_name[:-4],first_page,last_page)

        with open (output_filename,'wb')as f:
                pdf_writer.write(f)

        return pdf

#pdf.pdfSlice("frozen.pdf",1,3) #여러페이지 저장(1페이지부터 3페이까지 저장)
#pdf.pdfSlice("frozen.pdf",3) #한페이지만 저장        