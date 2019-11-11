import pandas as pd
import numpy as np

class data_file:
    def __init__(self,file_name,form):
        self.file_name=file_name
        self.form=form

        file=read_csv(file_name)
        #f=open(file_name,'r')
        #lines=f.readlines()
        #while True:
        #    line=f.readline()
        #    if not line: break
        #    print(line)
        #f.close()
        #for i in range(1,11):
        #    data="%d번째 줄입니다.\n"%i
        #    f.write(data)
        #f.close()


#csv파일
data_csv=pd.read_csv("diabetes.csv")
data_csv

#pdf파일
 #pdf파일 불러와서 text파일로 읽어들이기
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

def convert_pdf_to_txt(file_name):
    #pdf 리소스 매니저 객체 생성
    rsrcmgr=PDFResourceManager()
    #문자열 데이터를 파일처럼 처리하는 stringio->pdf 파일 내용이 여기 담김
    retstr=StringIO()
    codec='utf-8'
    laparams=LAParams()
    device=TextConverter(rsrcmgr,retstr,codec=codec,laparams=laparams)
    fp=open(file_name,'rb')
    interpreter=PDFPageInterpreter(rsrcmgr,device)
    password=""
    maxpages=0
    caching=True
    pagenos=set()
    
    for page in PDFPage.get_pages(fp,pagenos,maxpages-maxpages,password=password,caching=caching,check_extractable=True):
        interpreter.process_page(page)
    #text에 결과가 담김
    text=retstr.getvalue()
    
    fp.close()
    device.close()
    retstr.close()
    return text

v=convert_pdf_to_txt('Grade_컴퓨터구조.pdf')
print(v)
