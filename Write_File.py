#!usr/bin/env python3

import pandas as pd
import os

def write_excel(input_filepath,series: list):
    df = pd.concat(series,axis = 1)
    df.to_excel(input_filepath)
        
    
