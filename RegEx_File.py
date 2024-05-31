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
    line_nums = []
    for i,x in enumerate(content):
        found = []
        found = re.findall(r"c\w+\[\d+\]",x)
        if len(found) != 0 and found != None:
            line_nums.extend([i]*len(found))
            IO.extend(found)
    data = {

        "Line Numbers":line_nums,
        
        "I/O Ports": IO
    }
    df = pd.DataFrame(data)
    return df

def find_programs(content,existing = None):
    if type(existing) != pd.DataFrame:
        programs = []
        line_nums = []
        for i,x in enumerate(content):
            found = []
            found = re.findall(r"PROGRAM.+\(Description.+,",x)
            if len(found) != 0 and found != None:
                line_nums.extend([i]*len(found))
                programs.extend(found)
        data = {

            "Line Numbers":line_nums,

            "Program Names":programs

        }
        df = pd.DataFrame(data)
        return df
    else:
        existing["Program Names"] = ""
        programs = []
        indexes = []
        for i,x in enumerate(content):
            found = re.search(r"PROGRAM.+\Description.+,",x)
            if found:
                found = found.group()
            if found != None:
                programs.append(found)
                indexes.append(i)
        print("programs")
        programs.insert(0,"")
        indexes.append(len(content))
        pgstart = 0
        for pgnum,program in list(zip(indexes,programs)):

            print("(PGstart,Pgnum)",pgstart,pgnum)
            existing.loc[(existing["Line Numbers"]>pgstart) & (existing["Line Numbers"] < pgnum),["Program Names"]]=program
            
            pgstart+=int(pgnum)-pgstart

        return existing
            
if __name__ == "__main__":
    start_bool = prompt_start()
    if start_bool:
        filepath = prompt_filepath()
    to_process  = load_file(filepath)
    io_used = find_IO(to_process)
    df = io_used.to_frame()
    df.to_excel("test.xlsx")
