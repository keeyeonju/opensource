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
