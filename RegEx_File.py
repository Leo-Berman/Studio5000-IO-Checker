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
        
def do_regex(content):

    # declare lists and dicts for things to go in
    IO = []
    IO_pgnums = []
    programs = [""] # Extra placeholder for IO not in a Program
    programs_pgnums = []
    aliases = {}

    # iterate through each line
    for i,x in enumerate(content):

        # perform regex
        tmp_program = re.search(r"PROGRAM.+\Description.+,",x)
        tmp_IO = re.findall(r"c\w+\[\d+\]",x)
        tmp_alias =  re.search(r"(\w+) OF (.+\[.+])",x)

        # if it finds something add it to the appropriate variable (i+1 because python uses 0 indexing)
        if tmp_program:
            programs.append(tmp_program.group())
            programs_pgnums.append(i+1)
        if tmp_IO:
            IO.extend(tmp_IO)
            IO_pgnums.extend([i+1]*len(tmp_IO))
        if tmp_alias:
            tmp_alias=tmp_alias.group().strip()[1:].split()
            OF = tmp_alias[2]
            ALIAS = tmp_alias[0]
            if OF not in aliases:
                aliases[OF] = set()
                aliases[OF].add(ALIAS)
            else:
                aliases[OF].add(ALIAS)

    # Create dataframe with just IO and their respective Line Numbers
    data = {

        "Line Numbers":IO_pgnums,
        
        "I/O": IO
    }
    df = pd.DataFrame(data)

    # find maximum number of alias length
    max_alias_number = 0
    for x in list(aliases.values()):
        print(x,len(x))
        currlen = len(x)
        max_alias_number = len(x) if currlen > max_alias_number else max_alias_number

    # add columns for the aliases
    for i in range(max_alias_number):
        df["Alias"+str(i)]=""

    # fill in rows for aliases
    for x in aliases:
        for i,y in enumerate(aliases[x]):
            df.loc[df["I/O"]==x,["Alias"+str(i)]]=y
    
    # add a column for the program names
    df["Program Names"] = ""
    pgstart = 0
    for pgnum,program in list(zip(programs_pgnums,programs)):
        df.loc[(df["Line Numbers"]>pgstart) & (df["Line Numbers"] < pgnum),["Program Names"]]=program
        pgstart+=int(pgnum)-pgstart

    return df
    
if __name__ == "__main__":
    start_bool = prompt_start()
    if start_bool:
        filepath = prompt_filepath()
    to_process  = load_file(filepath)
    io_used = find_IO(to_process)
    df = io_used.to_frame()
    df.to_excel("test.xlsx")
