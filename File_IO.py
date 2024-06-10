# Import custom  libraries ( and pandas )
import User_Interactions as UI
import pandas as pd

# return contents of file, if empty, exit
def load_file(input_filepath):

    # Read the file in with proper encoding
    file = open(input_filepath,"r",encoding='UTF8')
    content = file.readlines()
    file.close()
    
    # If file was empty, abort, Otherwise return the contents of the file
    if content == None:
         UI.common_error("File was Empty")
    else:
        return content

def write_excel(input_filepath,df):

    # Write the excel file & tell the user their job was complete
    df.to_excel(input_filepath,index=False)
    UI.prompt("Your file was written to "+input_filepath,"End screen")
