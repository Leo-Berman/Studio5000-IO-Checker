#!usr/bin/env python3

import easygui as eg
import pandas as pd
import re

from Get_File import *

def load_file(input_filepath):
    file = open(input_filepath,"r",encoding='UTF8')
    content = file.readlines()
    for i,x in enumerate(content):
        content[i] = str(x.encode('utf-8'))
    file.close()
    if content == None:
         eg.msgbox("File was Empty","Process cancelling...","Exiting...")
    else:
        return content


def find_IO(content):
    IO = []
    indexes = []
    for i,x in enumerate(content):
        found = []
        found = re.findall(r"c\w+\[\d+\]",x)
        if len(found) != 0 and found != None:
            indexes.append(str(i))
            for j,x in enumerate(found[1:]):
                indexes.append(str(i)+"_"+str(j+1))
            IO.extend(found)
    io_used = pd.Series(IO,name="IO Used",index=indexes)
    return io_used

def find_programs(content):
    programs = []
    indexes = []
    for i,x in enumerate(content):
        found = []
        found = re.findall(r"PROGRAM.+\(Description.+,",x)
        if len(found) != 0 and found != None:
            indexes.extend([i]*len(found))
            programs.extend(found)
    programs_used = pd.Series(programs,name="Program Names",index = indexes)
    return programs_used

if __name__ == "__main__":
    start_bool = prompt_start()
    if start_bool:
        filepath = prompt_filepath()
    to_process  = load_file(filepath)
    io_used = find_IO(to_process)
    df = io_used.to_frame()
    df.to_excel("test.xlsx")
