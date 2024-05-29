from Get_File import *
from RegEx_File import *
from Write_File import *

def main():
    start_bool = prompt_start()
    if start_bool:
        filepath = prompt_filepath()
    to_process  = load_file(filepath)
    io_used = find_IO(to_process)
    write_excel(r"C:\Users\lberman\Desktop\PyRegEx\test.xlsx",[io_used])
    

if __name__ == "__main__":
    main()
