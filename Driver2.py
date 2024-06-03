from Get_File import *
from RegEx_File import *
from Write_File import *


def main():
    input_filepath = prompt_input_filepath()
    to_process = load_file(input_filepath)
    df = do_regex(to_process)
    output_filepath = prompt_output_filepath()
    write_excel(fr"{output_filepath}",df)

if __name__ == "__main__":
    main()
