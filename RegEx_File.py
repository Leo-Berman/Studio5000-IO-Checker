#!usr/bin/env python3

import easygui as eg
import pandas as pd
import re

from Get_File import *

def load_file(input_filepath):
    file = open(input_filepath,"r",encoding='UTF8')
    content = file.read()
    file.close()
    if content == None:
         eg.msgbox("File was Empty","Process cancelling...","Exiting...")
    else:
        return content


def find_IO(content):
    content = str(content.encode('utf-8'))
    IOs = sorted(list(set(re.findall("c\w+\[\d+\]",content))))
    io_used = pd.Series(IOs,name="IO Used")
    return io_used

if __name__ == "__main__":
    start_bool = prompt_start()
    if start_bool:
        filepath = prompt_filepath()
    to_process  = load_file(filepath)
    io_used = find_IO(to_process)
    df = io_used.to_frame()
    df.to_excel("test.xlsx")
