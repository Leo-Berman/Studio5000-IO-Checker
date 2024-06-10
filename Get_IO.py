# import custom libraries
import Data_Processing as DP
import User_Interactions as UI
import File_IO as FIO

def main():

    # Tell the user to select an L5K file
    UI.prompt("Please select an L5K file to process","L5K Selector")

    # Have the user select an L5K file
    input_filepath = UI.prompt_input_filepath()

    # Load the file into memory
    to_process = FIO.load_file(input_filepath)

    # Perform the processing of the data
    df = DP.do_regex(to_process)

    # Tell the user to select a folder
    UI.prompt("Please select an output folder","Output File Path Prompt")

    # Have the user select an output filepath
    output_filepath = UI.prompt_output_filepath()

    # Write the data frame
    FIO.write_excel(fr"{output_filepath}",df)

if __name__ == "__main__":
    main()
