import User_Interactions as UI
import pandas as pd

# Load the file into memory
def load_file(input_filepath,Verbose=False):

    # Read the file in with proper encoding
    file = open(input_filepath,"r",encoding='UTF8')
    content = file.readlines()

    # Iterate through and convert to unicode
    #for i,x in enumerate(content):
    #    content[i] = str(x.encode('utf-8'))

    # Close the file
    file.close()

    if Verbose == True:
        print(content)
    
    # If file was empty, abort
    if content == None:
         UI.common_error("File was Empty")

    # Otherwise return the contents of the file
    else:
        return content

# Output info from processed L5K file
def write_excel(input_filepath,df,Verbose = False):

    # Debugging purposes
    if Verbose == True:
        print(input_filepath)

    # Write the excel file
    df.to_excel(input_filepath,index=False)

    # Tell the user their job was complete
    UI.prompt("Your file was written to "+input_filepath,"End screen")
