from Get_File import *
from RegEx_File import *
from Write_File import *

def main():
    start_bool = prompt_start()
    if start_bool:
        input_filepath = prompt_input_filepath()
    to_process  = load_file(input_filepath)
    io_used = find_IO(to_process)
    output_filepath = prompt_output_filepath()
    write_excel(fr"{output_filepath}",[io_used])
    

if __name__ == "__main__":
    main()
