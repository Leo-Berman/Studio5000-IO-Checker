from Get_File import *
from RegEx_File import *
from Write_File import *

Verbose = False

def main():
    cont,selections = prompt_start()

    if Verbose == True:
        print("Selection = ",selections)

    if cont == True:
        input_filepath = prompt_input_filepath()
    to_process = load_file(input_filepath)

    if Verbose == True:
        print("Content = ",to_process)
        
    
    if "IO POINTS" in selections:
        df = find_IO(to_process)
    if "PROGRAM NAMES" in selections:
        if selections.index("PROGRAM NAMES") == 0:
            df = find_programs(to_process)
        else:
            df = find_programs(to_process,df)
    output_filepath = prompt_output_filepath()

    if Verbose == True:
        print(df)
    write_excel(fr"{output_filepath}",df)
    

if __name__ == "__main__":
    main()
