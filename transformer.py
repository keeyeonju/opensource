import pandas as pd
import numpy as np

from xml.etree.ElementTree import Element, SubElement, ElementTree, parse

from tabula import read_pdf #pip install tabula-py
import PyPDF2 #pip install PyPDF2

import os

class data:
    def open_data(name,xml_node1,xml_node2):
        if name[-3:]=='csv':
            csv_data=pd.read_csv(name)
            return csv_data
        
        elif name[-4:]=='json':
            json_data=pd.read_json(name,encoding="utf-8")
            return json_data
            
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


            
    def trans(name,form):
        if name[-3:]=='csv':
            thisfile=name
            base=os.path.splitext(thisfile)[0]
            os.rename(thisfile,base+"."+form)
            
        elif name[-4:]=='json':
            thisfile=name
            base=os.path.splitext(thisfile)[0]
            os.rename(thisfile,base+"."+form)
            
        elif name[-3:]=='xml':
            #xml->csv
            if form=='csv':
                result=name.to_csv("test.csv")
                return result
            #xml->json
            elif form=='json':
                result=name.to_csv("test.json")
                return result
            else:                       
                thisfile=name
                base=os.path.splitext(thisfile)[0]
                os.rename(thisfile,base+"."+form)
            
        elif name[-3:]=='pdf':
            thisfile=name
            base=os.path.splitext(thisfile)[0]
            os.rename(thisfile,base+"."+form)
