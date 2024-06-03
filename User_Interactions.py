import pandas as pd
import os
import easygui as eg

# Error bubble
def common_error(Reason = "",Verbose = False):

    if Verbose == True:
        print(Reason)
    
    eg.msgbox(Reason+" Process cancelling...","Exiting...")
    exit()


# prompt the user for the output filepath
def prompt_output_filepath(Verbose=False):

    # Have the user select the folder
    output_folder = eg.diropenbox(msg="Select Output Folder",title="Output Folder Request")


    # Debugging purposes
    if Verbose == True:
        print("Output path = ", output_folder)

    # If there is no output folder, abort
    if output_folder == None:
        common_error("No output folder selected")

    # Have the user enter the name of a file
    filename = eg.textbox(msg="Enter the name of the file to save",title="Output File Request")

    # If there is no filename, abort
    if filename == None:
        common_error("No Filename")

    # Otherwise make sure the file has the correct extension
    elif filename.endswith(".xlsx"):
        return output_folder + "\\" + filename
    else:
        return output_folder + "\\" + filename + ".xlsx"

# Simple msg box wrapper to guide the user
def prompt(inmsg,intitle,okbtn="ok",Verbose=False):

    if Verbose == True:
        print("In message = ",inmsg,"In title = ",intitle,"Ok button = ",okbtn)
    
    output = eg.msgbox(inmsg,intitle,okbtn)
    if output!=okbtn:
        common_error("Program Exited")

# Getting the L5K filepath to process
def prompt_input_filepath(Verbose=False):

    # Prompt the user
    input_path = eg.fileopenbox(title = "Select a file", default="*.L5K")

    # If no path then abort
    if input_path == None:
        common_error("No L5K file selected")

    if not input_path.endswith(".L5K"):
        common_error("File selected is not an L5K file")
    
    # Otherwise return the path
    else:

        # Debugging Purposes
        if Verbose == True:
            print("Input path = ", input_path)
        
        return input_path

