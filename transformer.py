import pandas as pd
import numpy as np

from xml.etree.ElementTree import Element, SubElement, ElementTree, parse

from tabula import read_pdf #pip install tabula-py
import PyPDF2 #pip install PyPDF2

import os

import pdfkit

from PyPDF2 import PdfFileReader, PdfFileWriter

class data:
    def open_data(name,xml_node1,xml_node2):
        #csv
        if name[-3:]=='csv':
            csv_data=pd.read_csv(name)
            return csv_data

        #json
        elif name[-4:]=='json':
            json_data=pd.read_json(name,encoding="utf-8")
            return json_data

        #xml
        elif name[-3:]=='xml':
            tree = parse(name) #xml 파일 가져오기
            root = tree.getroot() #root 노드 가져오기

            ch=root.findall(xml_node1) #일치하는 모든 노드 가져오기

            rows=[]
            for node in ch:
                dt=node.find(xml_node2).text
                rows.append({xml_node2:dt})

            xml_data=pd.DataFrame(rows,columns=[xml_node2])
            return xml_data

        #pdf
        elif name[-3:]=='pdf':
            reader = PyPDF2.PdfFileReader(open(name, mode='rb')) 
            m = reader.getNumPages() 
            #print(reader) 
            print(m) 
            for i in range(m): 
                n = i+1 

                if n==1: 
                    df = read_pdf(name, pandas_options={'header': None, 'error_bad_lines': False}, pages=n) 
                    index = np.where(df[0].isnull())[0] 
                    sect = df.iloc[index[0]:index[-1]] 
                    s = [] 
                    headers = [] 
                    for col in sect: 
                        colnames = sect[col].dropna().values.flatten() 
                        s.insert(len(s), colnames)
                        pic = [' '.join(s[col])] 
                        for i in pic: 
                               headers.append(i) 
                    print(df) 
                    df.drop(sect, inplace=True) 
                    df.columns = headers 
                    new_df = pd.DataFrame(columns=headers) 
                    new_df = pd.concat([new_df, df], axis=0, ignore_index=True) 

                else: 
                    df_2 = read_pdf(name, pandas_options={'header': None, 'error_bad_lines': False, 'encoding': "ISO-8859-1"}, pages=n) 
                    df_2.drop(sect, inplace=True) 
                    df_2.columns = headers 
                    new_df = pd.concat([new_df, df_2], axis=0, ignore_index=True) 
            
            new_df.columns = headers 
            print(new_df) 
            new_df.to_csv(name, index=False)
            


    #변환함수   
    def trans(name,form):
        
        #상호변환
        if form!='pdf':
            thisfile=name
            base=os.path.splitext(thisfile)[0]
            os.rename(thisfile,base+"."+form)
        
        #html->pdf
        elif name[-4:]=='html' and form=='pdf':
            thisfile=name
            base=os.path.splitext(thisfile)[0]
            pdfkit.from_file(thisfile,base+"."+form)


    #여러 형식의 데이터를 데이터프레임로 변환하여 사용한 후 원하는 형식의 데이터로 변환 
    def trans_dataframe(name,form,new_name):
            result=name.to_csv(new_name+"."+form)
            return result



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




        
        
