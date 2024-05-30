#!usr/bin/env python3

import easygui as eg

Verbose=True

def prompt_start():
    choices = eg.multchoicebox(msg = "Please select all preferred outputs...",choices = ["IO POINTS","PROGRAM NAMES"])
    start_bool = eg.msgbox(msg="Please select an L5K file...")

    if choices != None:
        return True,choices
    else:
        return False,choices

def prompt_input_filepath():

    input_path = eg.fileopenbox(title = "Select a file", default="*.L5K")
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
