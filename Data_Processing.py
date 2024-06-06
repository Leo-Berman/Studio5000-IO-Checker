#!usr/bin/env python3

import easygui as eg
import pandas as pd
import re

# perform the data processing
def do_regex(content,Verbose = False):

    # declare lists and dicts for things to go in
    IO = []
    IO_pgnums = []
    programs = [""] # Extra placeholder for IO not in a Program
    programs_pgnums = []
    aliases = {}
    held_program = "N/A"
    # iterate through each line
    for i,x in enumerate(content):

        # perform regex
        tmp_program = re.search(r'(PROGRAM \w+)(?= \(Description := ".+",)',x)
        tmp_IO = re.findall(r"(?<= )(c\w+\[.+\])",x)
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
            OF = tmp_alias[2]+"SPLIT"+held_program
            ALIAS = tmp_alias[0]
            if OF not in aliases:
                aliases[OF] = set()
                aliases[OF].add(ALIAS)
            else:
                aliases[OF].add(ALIAS)
        if tmp_program != None:
            held_program = tmp_program.group()
    # Create dataframe with just IO and their respective Line Numbers
    data = {

        "Line Numbers":IO_pgnums,
        
        "I/O": IO
    }
    df = pd.DataFrame(data)

    # add a column for the program names
    df["Program Names"] = ""
    pgstart = 0
    for pgnum,program in list(zip(programs_pgnums,programs)):
        df.loc[(df["Line Numbers"]>pgstart) & (df["Line Numbers"] < pgnum),["Program Names"]]=program
        pgstart+=int(pgnum)-pgstart
    
    # find maximum number of alias length
    max_alias_number = 0
    for x in list(aliases.values()):
        currlen = len(x)
        max_alias_number = len(x) if currlen > max_alias_number else max_alias_number
        
        # Debugging purposes
        if Verbose == True:
            if currlen > max_alias_number:
                print(x,len(x))
                pass
            
    if Verbose == True:
        print("Maximum number of aliases = ",max_alias_number)

    # add columns for the aliases
    for i in range(max_alias_number):
        df["Alias"+str(i)]=""

    # fill in rows for aliases
    for x in aliases:
        split_parts = x.split("SPLIT")
        alias_part = split_parts[0]
        program_part = split_parts[1]
        print(program_part)
        for i,y in enumerate(aliases[x]):
            
            
            df.loc[(df["I/O"]==alias_part) &(df["Program Names"]==program_part),["Alias"+str(i)]]=y
    
    

    return df
    
