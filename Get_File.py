#!usr/bin/env python3

import easygui as eg

Verbose=True

def prompt_start():
    start_bool = eg.ynbox("Would you like to begin code checks?","Begin Checks", ("Yes", "No"))
    if start_bool:
        return True
    else:
        eg.msgbox("Process cancelling...","Exiting...")
        return False

def prompt_filepath():

    input_path = eg.fileopenbox(title = "Open a file", default="*.L5K")
    if input_path == None:
        eg.msgbox("Process cancelling...","Exiting...")
        return False
    else:
        if Verbose == True:
            print("Input path = ", input_path)
        return input_path
    
  
if __name__ == "__main__":
    start_bool = prompt_start()
    if Verbose == True:
        print("Start Bool = ",start_bool)
    if start_bool == True:
        files = prompt_filepath()
