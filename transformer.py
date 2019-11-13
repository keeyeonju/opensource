import pandas as pd
import numpy as np
from xml.etree.ElementTree import Element, SubElement, ElementTree, parse

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

    #def to_pdf():
