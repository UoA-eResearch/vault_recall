#!/usr/bin/env python3
from tqdm import tqdm
from tqdm.contrib.concurrent import thread_map

from glob import glob
import sys
import time
import pandas as pd

# first argument should be a text file containing files to check. Such as one generated by:
# find . -type f > filelist.txt
files = list(pd.read_table(sys.argv[1], header=None).iloc[:, 0])

def read_file(filename):
    while True:
        try:
            with open(filename, "rb") as f:
                f.read(1)
            return
        except Exception as e:
            print(f"{e} for {filename}, retrying in 10s")
            time.sleep(10)

thread_map(read_file, files, max_workers=32)
