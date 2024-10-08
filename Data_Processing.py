# import libraries
import easygui as eg
import pandas as pd
import re

'''
Go through file and collect:
    all IO points
    their page numbers
    affiliated program
    and aliases used within that program

Returns a pandas DataFrame
'''
def do_regex(content,Verbose = False):

    # declare lists and dicts for things to go in
    IO = []
    IO_pgnums = []
    programs = [""] # Extra placeholder for IO not in a Program
    programs_pgnums = []
    aliases = {}
    held_program = "N/A"

    # iterate through each line in L5K file
    for i,x in enumerate(content):

        '''
        Use regular expression matching to check the line for:
            A new program
            An IO point
            An alias
        '''
        tmp_program = re.search(r'(PROGRAM \w+)((?= \((Description) := .+,)|(?= \((MODE) := .+,)|(?= \((MAIN) := .+,))',x)
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

            # split alias into actual IO point, and what the alias is of that IO point
            tmp_alias=tmp_alias.group().strip().split()

            # This lets us identy by IO and program later on
            OF = tmp_alias[2]+"SPLIT"+held_program

            # Adds the alias into a dictionary using the IO and program as a key
            ALIAS = tmp_alias[0]
            if OF not in aliases:
                aliases[OF] = set()
                aliases[OF].add(ALIAS)
            else:
                aliases[OF].add(ALIAS)

        # if there is a new program, save it to be used until the end of the program
        if tmp_program != None:
            held_program = tmp_program.group()

        # If the program ends, clear out the held_program, and make the current program ""
        if "END_PROGRAM" in x:
            programs.append("")
            programs_pgnums.append(i+1)
            held_program = ""

    # Create dataframe with just IO and their respective Line Numbers
    data = {

        "Line Numbers":IO_pgnums,
        
        "I/O": IO
    }
    df = pd.DataFrame(data)

    # add a column for the program names
    df["Program Names"] = ""

    # iterate through and check using page numbers which IO point belongs to which program
    pgstart = 0
    for pgnum,program in list(zip(programs_pgnums,programs)):
        df.loc[(df["Line Numbers"]>pgstart) & (df["Line Numbers"] < pgnum),["Program Names"]]=program
        pgstart+=int(pgnum)-pgstart
    
    # find maximum number of alias length so we know how many colums to add
    max_alias_number = 0
    for x in list(aliases.values()):
        currlen = len(x)
        max_alias_number = currlen if currlen > max_alias_number else max_alias_number
        

        

    # add columns for the aliases
    for i in range(max_alias_number):
        df["Alias"+str(i)]=""

    # fill in rows for aliases
    for x in aliases:
        split_parts = x.split("SPLIT")
        alias_part = split_parts[0]
        program_part = split_parts[1]
        for i,y in enumerate(aliases[x]):
            
            
            df.loc[(df["I/O"]==alias_part) &(df["Program Names"]==program_part),["Alias"+str(i)]]=y
    
    
    # return the dataframe
    return df
    
