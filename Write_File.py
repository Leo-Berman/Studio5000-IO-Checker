#!usr/bin/env python3

import pandas as pd
import os
import easygui as eg

from CommonError import *

Verbose = True

def write_excel(input_filepath,df):
    if Verbose == True:
        print(input_filepath)
    df.to_excel(input_filepath)
    eg.msgbox(msg="Your file was written to "+input_filepath)

def prompt_output_filepath():
    eg.msgbox(msg="Please select an output folder")
    output_folder = eg.diropenbox(msg="Select Output Folder",title="Output Folder Request")

    if output_folder == None:
        common_error()
        return None
    else:
        if Verbose == True:
            print("Output path = ", output_folder)

    filename = eg.textbox(msg="Enter the name of the file to save",title="Output File Request")
    if filename == None:
        common_error()
        return None
    elif filename.endswith(".xlsx"):
        return output_folder + "\\" + filename
    else:
        return output_folder + "\\" + filename + ".xlsx" 
if __name__ == "__main__":
    prompt_output_filepath()
