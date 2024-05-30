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
        
    excel_out = []
    
    if "IO POINTS" in selections:
        excel_out.append(find_IO(to_process))
    if "PROGRAM NAMES" in selections:
        excel_out.append(find_programs(to_process))
    
    output_filepath = prompt_output_filepath()

    if Verbose == True:
        print(excel_out)
    write_excel(fr"{output_filepath}",excel_out)
    

if __name__ == "__main__":
    main()
