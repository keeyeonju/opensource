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


#---CSV 파일---
data_csv=pd.read_csv("diabetes.csv")
data_csv


#---JSON 파일----
#json파일 생성하기
import json
from collections import OrderedDict

group_data = OrderedDict()
albums = OrderedDict()
 
group_data["name"] = "여자친구"
group_data["members"] = ["소원", "예린", "은하", "유주", "신비", "엄지"]
 
albums["EP 1집"] = "Season of Glass"
albums["EP 2집"] = "Flower Bud"
albums["EP 3집"] = "Snowflake"
albums["정규 1집"] = "LOL"
albums["EP 4집"] = "THE AWAKENING"
 
group_data["albums"] = albums

# Print JSON
print(json.dumps(group_data, ensure_ascii=False, indent="\t") )

#json파일 저장
with open('gfriend.json', 'w', encoding="utf-8") as make_file:
    json.dump(group_data, make_file, ensure_ascii=False, indent="\t")

#json파일 열기
json_data=open('C:/Users/quftp/Desktop/2019/2학기/오픈소스개론/프로젝트/gfriend.json',encoding='UTF8').read()

data=json.loads(json_data)
print(data)


#---XML 파일---
# xml파일 파싱
from xml.etree.ElementTree import parse

tree = parse('test.xml') #xml파일 가져오기
root = tree.getroot() #root 노드 가져오기

student = root.findall("student") #일치하는 모든 노드 가져오기
#값을 가져오고 싶다면 -> student.find("name").text
#일치하는 첫번재 노드의 속성 가져오기 -> student.findetext('score').attrib

name = [x.findtext("name") for x in student]
age = [x.findtext("age") for x in student]
score = [x.find("score").attrib for x in student]

print(name)
print(age)
print(score)


#---PDF 파일---
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
