#!usr/bin/env python3

import pandas as pd
import os
import easygui as eg

from Get_File.py import *
from CommonError import *

# Debugging Purposes
Verbose = False

# Output info from processed L5K file
def write_excel(input_filepath,df):

    # Debugging purposes
    if Verbose == True:
        print(input_filepath)

    # Write the excel file
    df.to_excel(input_filepath,index=False)

    # Tell the user their job was complete
    prompt("Your file was written to "+input_filepath,"End screen")
