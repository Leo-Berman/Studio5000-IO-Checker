import pandas as pd
import os
import easygui as eg

# If valid, return True, else return False
def test_valid_filename(inname):

    # Check for printable invalid windows characters
    invalid_chars = ['<','>',':','"','/','\\','|','?','*',]
    for x in invalid_chars:
        if inname.__contains__(x):
            return False

    # Check for non printable invalid windows characters (chr converts from decimal to ascii)
    for i in range(32):
        if inname.__contains__(chr(i)):
            return False

    return True
            
def common_error(Reason = ""):
    
    eg.msgbox(Reason+" Process cancelling...","Exiting...")

    exit()

# return filepath, if failed, exit
def prompt_output_filepath():

    # Have the user select the folder
    output_folder = eg.diropenbox(msg="Select Output Folder",title="Output Folder Request")

    # If there is no output folder, abort
    if output_folder == None:
        common_error("No output folder selected")

    # Have the user enter the name of a file
    filename = eg.textbox(msg="Enter the name of the file to save",title="Output File Request")

    # If there is no filename, abort
    if filename == None:
        common_error("No Filename")

    # If they keep trying to put an invalid name in, keep asking
    # However, if they cancel stop
    #
    while test_valid_filename(filename) == False:
        filename = eg.textbox(msg="You entered a filename with invalid characters, please try again",title="Output File Request Try Again")
        if filename == None:
            common_error("No Filename")
            
    # Make sure the file has the correct extension
    if filename.endswith(".xlsx"):
        return output_folder + "\\" + filename
    else:
        return output_folder + "\\" + filename + ".xlsx"

# if user doesn't click ok, exit
def prompt(inmsg,intitle,okbtn="ok"):

    # get the user's response to the msgbox
    output = eg.msgbox(inmsg,intitle,okbtn)

    # if they don't click ok, exit the program
    if output!=okbtn:
        common_error("Program Exited")

# return L5K filepath, if failed, exit
def prompt_input_filepath():

    # Prompt the user
    input_path = eg.fileopenbox(title = "Select a file", default="*.L5K")

    # If no path or not an L5k Otherwise return the path
    if input_path == None:
        common_error("No L5K file selected")
    elif not input_path.endswith(".L5K"):
        common_error("File selected is not an L5K file")
    else:        
        return input_path

